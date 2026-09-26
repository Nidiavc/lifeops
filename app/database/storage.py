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