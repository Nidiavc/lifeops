import sqlite3
from pathlib import Path


class Storage:

    def __init__(self):
        app_directory = Path(__file__).resolve().parents[1]
        database_path = app_directory / "lifeops.db"

        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            unit TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS metric_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metric_name TEXT,
            value REAL,
            entry_date TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            progress INTEGER
        )
        """)

        self.connection.commit()

        self.ensure_entry_date_column()

    def ensure_entry_date_column(self):

        columns = self.cursor.execute(
            "PRAGMA table_info(metric_entries)"
        ).fetchall()

        column_names = [
            column[1]
            for column in columns
        ]

        if "entry_date" not in column_names:
            self.cursor.execute("""
            ALTER TABLE metric_entries
            ADD COLUMN entry_date TEXT
            """)

            self.connection.commit()

            print("Column entry_date added to metric_entries.")

    # ==========================
    # EXISTS
    # ==========================

    def metric_exists(self, metric_name):

        result = self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM metrics
            WHERE name = ?
            """,
            (metric_name,)
        )

        return result.fetchone()[0] > 0

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
        metric_name,
        value,
        entry_date
    ):

        result = self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM metric_entries
            WHERE metric_name = ?
            AND value = ?
            AND entry_date = ?
            """,
            (
                metric_name,
                value,
                entry_date
            )
        )

        return result.fetchone()[0] > 0

    # ==========================
    # SAVE
    # ==========================

    def save_metric(self, metric):

        if self.metric_exists(metric.name):
            return

        self.cursor.execute(
            """
            INSERT INTO metrics(name, unit)
            VALUES (?, ?)
            """,
            (
                metric.name,
                metric.unit
            )
        )

        self.connection.commit()

        print(f"Metric saved: {metric.name}")

    def save_metric_entry(
        self,
        metric_name,
        value,
        entry_date
    ):

        if self.metric_entry_exists(
            metric_name,
            value,
            entry_date
        ):
            return

        self.cursor.execute(
            """
            INSERT INTO metric_entries(
                metric_name,
                value,
                entry_date
            )
            VALUES (?, ?, ?)
            """,
            (
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
            INSERT INTO goals(title, progress)
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
    # SHOW
    # ==========================

    def show_metrics(self):

        results = self.cursor.execute(
            """
            SELECT id, name, unit
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
                id,
                metric_name,
                value,
                entry_date
            FROM metric_entries
            ORDER BY id
            """
        )

        for row in results:
            print(row)

    def show_goals(self):

        results = self.cursor.execute(
            """
            SELECT id, title, progress
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

        result = self.cursor.execute(
            """
            SELECT AVG(value)
            FROM metric_entries
            WHERE metric_name = ?
            """,
            (metric_name,)
        )

        average = result.fetchone()[0]

        if average is None:
            return 0

        return average

    def get_metric_latest_value(self, metric_name):

        result = self.cursor.execute(
            """
            SELECT value
            FROM metric_entries
            WHERE metric_name = ?
            ORDER BY
                CASE
                    WHEN entry_date IS NULL THEN 1
                    ELSE 0
                END,
                entry_date DESC,
                id DESC
            LIMIT 1
            """,
            (metric_name,)
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

        result = self.cursor.execute(
            """
            SELECT AVG(value)
            FROM metric_entries
            WHERE metric_name = ?
            AND entry_date = ?
            """,
            (
                metric_name,
                entry_date
            )
        )

        average = result.fetchone()[0]

        if average is None:
            return 0

        return average

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

    def close(self):
        self.connection.close()