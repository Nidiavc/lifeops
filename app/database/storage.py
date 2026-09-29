import sqlite3


class Storage:

    def __init__(self):
        self.connection = sqlite3.connect("lifeops.db")
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
            value REAL
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

    def save_metric(self, metric):

        self.cursor.execute(
            """
            INSERT INTO metrics(name, unit)
            VALUES (?, ?)
            """,
            (metric.name, metric.unit)
        )

        self.connection.commit()

        print(f"Metric saved: {metric.name}")

    def save_metric_entry(self, metric_name, value):

        self.cursor.execute(
            """
            INSERT INTO metric_entries(metric_name, value)
            VALUES (?, ?)
            """,
            (metric_name, value)
        )

        self.connection.commit()

    def save_goal(self, goal):

        self.cursor.execute(
            """
            INSERT INTO goals(title, progress)
            VALUES (?, ?)
            """,
            (goal.title, goal.progress)
        )

        self.connection.commit()

        print(f"Goal saved: {goal.title}")

    def show_metrics(self):

        results = self.cursor.execute(
            "SELECT * FROM metrics"
        )

        for row in results:
            print(row)

    def show_metric_entries(self):

        results = self.cursor.execute(
            "SELECT * FROM metric_entries"
        )

        for row in results:
            print(row)

    def show_goals(self):

        results = self.cursor.execute(
            "SELECT * FROM goals"
        )

        for row in results:
            print(row)

    def get_metric_average(self, metric_name):

        result = self.cursor.execute(
            """
            SELECT AVG(value)
            FROM metric_entries
            WHERE metric_name = ?
            """,
            (metric_name,)
        )

        return result.fetchone()[0]

    def get_metric_latest_value(self, metric_name):

        result = self.cursor.execute(
            """
            SELECT value
            FROM metric_entries
            WHERE metric_name = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (metric_name,)
        )

        row = result.fetchone()

        if row:
            return row[0]

        return 0

    def get_goal_average_progress(self):

        result = self.cursor.execute(
            """
            SELECT AVG(progress)
            FROM goals
            """
        )

        return result.fetchone()[0]

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

        return result.fetchone()[0]

    def get_goal_min_progress(self):

        result = self.cursor.execute(
            """
            SELECT MIN(progress)
            FROM goals
            """
        )

        return result.fetchone()[0]