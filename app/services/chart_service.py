from pathlib import Path

import matplotlib.pyplot as plt


class ChartService:

    def create_history_chart(
        self,
        metric_name,
        history
    ):

        if not history:
            return

        dates = [
            row[0]
            for row in history
        ]

        values = [
            row[1]
            for row in history
        ]

        plt.figure(
            figsize=(10, 5)
        )

        plt.plot(
            dates,
            values,
            marker="o"
        )

        plt.title(
            f"{metric_name} History"
        )

        plt.xlabel(
            "Date"
        )

        plt.ylabel(
            metric_name
        )

        plt.grid(True)

        charts_path = (
            Path(__file__)
            .resolve()
            .parents[1]
            / "charts"
        )

        charts_path.mkdir(
            exist_ok=True
        )

        file_name = (
            metric_name.lower()
            .replace(" ", "_")
            + ".png"
        )

        full_path = (
            charts_path
            / file_name
        )

        plt.savefig(full_path)

        plt.close()

        print(
            f"Chart created: "
            f"{full_path}"
        )