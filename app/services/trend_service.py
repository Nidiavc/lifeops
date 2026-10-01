class TrendService:
    def calculate_trend(self, history):
        if len(history) < 2:
            return "Insufficient data"

        previous_average = history[-2][1]
        latest_average = history[-1][1]

        if latest_average > previous_average:
            return "Increasing"

        if latest_average < previous_average:
            return "Decreasing"

        return "Stable"

    def get_change(self, history):
        if len(history) < 2:
            return 0

        previous_average = history[-2][1]
        latest_average = history[-1][1]

        return latest_average - previous_average

    def get_percentage_change(self, history):
        if len(history) < 2:
            return 0

        previous_average = history[-2][1]
        latest_average = history[-1][1]

        if previous_average == 0:
            return 0

        difference = latest_average - previous_average

        return (
            difference / previous_average
        ) * 100

    def display(self, metric_name, history):
        print(f"\n{metric_name.upper()} TREND")
        print("======================")

        if len(history) < 2:
            print(
                "Insufficient dated records "
                "to calculate a trend."
            )
            return

        trend = self.calculate_trend(history)
        change = self.get_change(history)
        percentage_change = (
            self.get_percentage_change(history)
        )

        previous_date = history[-2][0]
        previous_average = history[-2][1]

        latest_date = history[-1][0]
        latest_average = history[-1][1]

        print(
            f"Previous date: {previous_date}"
        )

        print(
            f"Previous average: "
            f"{previous_average:.2f}"
        )

        print(
            f"Latest date: {latest_date}"
        )

        print(
            f"Latest average: "
            f"{latest_average:.2f}"
        )

        print(
            f"Change: {change:.2f}"
        )

        print(
            f"Percentage change: "
            f"{percentage_change:.2f}%"
        )

        print(
            f"Trend: {trend}"
        )