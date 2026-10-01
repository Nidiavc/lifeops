import sqlite3
from pathlib import Path


class Storage:
    def __init__(self):
        app_directory = Path(__file__).resolve().parents[1]
        database_path = app_directory / "lifeops.db"

        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

        self.cursor.execute("PRAGMA foreign_keys = ON")

    # ==========================
    # TABLES
    # ==========================

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                unit TEXT
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS metric_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                metric_name TEXT,
                value REAL,
                entry_date TEXT,
                metric_id INTEGER
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                progress INTEGER
            )
            """
        )

        self.connection.commit()

        self.ensure_entry_date_column()
        self.ensure_metric_id_column()
        self.backfill_metric_ids()

    # ==========================
    # DATABASE MIGRATIONS
    # ==========================

    def get_table_columns(self, table_name):
        columns = self.cursor.execute(
            f"PRAGMA table_info({table_name})"
        ).fetchall()

        return [column[1] for column in columns]

    def ensure_entry_date_column(self):
        column_names = self.get_table_columns(
            "metric_entries"
        )

        if "entry_date" not in column_names:
            self.cursor.execute(
                """
                ALTER TABLE metric_entries
                ADD COLUMN entry_date TEXT
                """
            )

            self.connection.commit()

            print(
                "Column entry_date added "
                "to metric_entries."
            )

    def ensure_metric_id_column(self):
        column_names = self.get_table_columns(
            "metric_entries"
        )

        if "metric_id" not in column_names:
            self.cursor.execute(
                """
                ALTER TABLE metric_entries
                ADD COLUMN metric_id INTEGER
                """
            )

            self.connection.commit()

            print(
                "Column metric_id added "
                "to metric_entries."
            )

    def backfill_metric_ids(self):
        self.cursor.execute(
            """
            UPDATE metric_entries
            SET metric_id = (
                SELECT MIN(metrics.id)
                FROM metrics
                WHERE metrics.name =
                      metric_entries.metric_name
            )
            WHERE metric_id IS NULL
            """
        )

        self.connection.commit()

    # ==========================
    # METRIC LOOKUP
    # ==========================

    def get_metric_id(self, metric_name):
        result = self.cursor.execute(
            """
            SELECT MIN(id)
            FROM metrics
            WHERE name = ?
            """,
            (metric_name,)
        )

        row = result.fetchone()

        if row and row[0] is not None:
            return row[0]

        return None

    # ==========================
    # EXISTS
    # ==========================

    def metric_exists(self, metric_name):
        return self.get_metric_id(
            metric_name
        ) is not None

    def goal_exists(self, title):
        result = self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM goals
            WHERE title = ?
            """,
            (title,)
        )

        return result.fetchone()[0] > 0

    def metric_entry_exists(
        self,
        metric_id,
        value,
        entry_date
    ):
        result = self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM metric_entries
            WHERE metric_id = ?
              AND value = ?
              AND entry_date = ?
            """,
            (
                metric_id,
                value,
                entry_date
            )
        )

        return result.fetchone()[0] > 0

    # ==========================
    # SAVE
    # ==========================

    def save_metric(self, metric):
        existing_metric_id = self.get_metric_id(
            metric.name
        )

        if existing_metric_id is not None:
            return existing_metric_id

        self.cursor.execute(
            """
            INSERT INTO metrics (
                name,
                unit
            )
            VALUES (?, ?)
            """,
            (
                metric.name,
                metric.unit
            )
        )

        self.connection.commit()

        print(f"Metric saved: {metric.name}")

        return self.cursor.lastrowid

    def save_metric_entry(
        self,
        metric_name,
        value,
        entry_date
    ):
        metric_id = self.get_metric_id(
            metric_name
        )

        if metric_id is None:
            raise ValueError(
                f"Metric not found: {metric_name}"
            )

        if self.metric_entry_exists(
            metric_id,
            value,
            entry_date
        ):
            return

        self.cursor.execute(
            """
            INSERT INTO metric_entries (
                metric_id,
                metric_name,
                value,
                entry_date
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                metric_id,
                metric_name,
                value,
                entry_date
            )
        )

        self.connection.commit()

    def save_goal(self, goal):
        if self.goal_exists(goal.title):
            return

        self.cursor.execute(
            """
            INSERT INTO goals (
                title,
                progress
            )
            VALUES (?, ?)
            """,
            (
                goal.title,
                goal.progress
            )
        )

        self.connection.commit()

        print(f"Goal saved: {goal.title}")

    # ==========================
    # SHOW DATA
    # ==========================

    def show_metrics(self):
        results = self.cursor.execute(
            """
            SELECT
                id,
                name,
                unit
            FROM metrics
            ORDER BY id
            """
        )

        for row in results:
            print(row)

    def show_metric_entries(self):
        results = self.cursor.execute(
            """
            SELECT
                metric_entries.id,
                metric_entries.metric_id,
                metrics.name,
                metric_entries.value,
                metric_entries.entry_date
            FROM metric_entries
            LEFT JOIN metrics
                ON metrics.id =
                   metric_entries.metric_id
            ORDER BY metric_entries.id
            """
        )

        for row in results:
            print(row)

    def show_goals(self):
        results = self.cursor.execute(
            """
            SELECT
                id,
                title,
                progress
            FROM goals
            ORDER BY id
            """
        )

        for row in results:
            print(row)

    # ==========================
    # METRIC STATISTICS
    # ==========================

    def get_metric_average(self, metric_name):
        metric_id = self.get_metric_id(
            metric_name
        )

        if metric_id is None:
            return 0

        result = self.cursor.execute(
            """
            SELECT AVG(value)
            FROM metric_entries
            WHERE metric_id = ?
            """,
            (metric_id,)
        )

        average = result.fetchone()[0]

        if average is None:
            return 0

        return average

    def get_metric_latest_value(
        self,
        metric_name
    ):
        metric_id = self.get_metric_id(
            metric_name
        )

        if metric_id is None:
            return 0

        result = self.cursor.execute(
            """
            SELECT value
            FROM metric_entries
            WHERE metric_id = ?
            ORDER BY
                CASE
                    WHEN entry_date IS NULL
                    THEN 1
                    ELSE 0
                END,
                entry_date DESC,
                id DESC
            LIMIT 1
            """,
            (metric_id,)
        )

        row = result.fetchone()

        if row:
            return row[0]

        return 0

    def get_metric_average_by_date(
        self,
        metric_name,
        entry_date
    ):
        metric_id = self.get_metric_id(
            metric_name
        )

        if metric_id is None:
            return 0

        result = self.cursor.execute(
            """
            SELECT AVG(value)
            FROM metric_entries
            WHERE metric_id = ?
              AND entry_date = ?
            """,
            (
                metric_id,
                entry_date
            )
        )

        average = result.fetchone()[0]

        if average is None:
            return 0

        return average

    def get_metric_history(self, metric_name):
        metric_id = self.get_metric_id(
            metric_name
        )

        if metric_id is None:
            return []

        results = self.cursor.execute(
            """
            SELECT
                entry_date,
                AVG(value) AS average_value
            FROM metric_entries
            WHERE metric_id = ?
              AND entry_date IS NOT NULL
            GROUP BY entry_date
            ORDER BY entry_date
            """,
            (metric_id,)
        )

        return results.fetchall()

    # ==========================
    # GOAL STATISTICS
    # ==========================

    def get_goal_average_progress(self):
        result = self.cursor.execute(
            """
            SELECT AVG(progress)
            FROM goals
            """
        )

        average = result.fetchone()[0]

        if average is None:
            return 0

        return average

    def get_goal_count(self):
        result = self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM goals
            """
        )

        return result.fetchone()[0]

    def get_goal_max_progress(self):
        result = self.cursor.execute(
            """
            SELECT MAX(progress)
            FROM goals
            """
        )

        maximum = result.fetchone()[0]

        if maximum is None:
            return 0

        return maximum

    def get_goal_min_progress(self):
        result = self.cursor.execute(
            """
            SELECT MIN(progress)
            FROM goals
            """
        )

        minimum = result.fetchone()[0]

        if minimum is None:
            return 0

        return minimum

    # ==========================
    # CONNECTION
    # ==========================

    def close(self):
        self.connection.close()