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

    def show_metrics(self):

        results = self.cursor.execute(
            "SELECT * FROM metrics"
        )

        for row in results:
            print(row)