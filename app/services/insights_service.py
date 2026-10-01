class InsightsService:
    def get_highest_day(self, history):
        if not history:
            return None

        return max(
            history,
            key=lambda record: record[1]
        )

    def get_lowest_day(self, history):
        if not history:
            return None

        return min(
            history,
            key=lambda record: record[1]
        )

    def get_historical_average(self, history):
        if not history:
            return 0

        total = sum(
            average_value
            for _, average_value in history
        )

        return total / len(history)

    def get_total_days(self, history):
        return len(history)

    def display(self, metric_name, history):
        print(f"\n{metric_name.upper()} INSIGHTS")
        print("======================")

        if not history:
            print(
                "No dated records available "
                "for insights."
            )
            return

        highest_day = self.get_highest_day(
            history
        )

        lowest_day = self.get_lowest_day(
            history
        )

        historical_average = (
            self.get_historical_average(
                history
            )
        )

        total_days = self.get_total_days(
            history
        )

        highest_date = highest_day[0]
        highest_average = highest_day[1]

        lowest_date = lowest_day[0]
        lowest_average = lowest_day[1]

        print(
            f"Highest average date: "
            f"{highest_date}"
        )

        print(
            f"Highest average: "
            f"{highest_average:.2f}"
        )

        print(
            f"Lowest average date: "
            f"{lowest_date}"
        )

        print(
            f"Lowest average: "
            f"{lowest_average:.2f}"
        )

        print(
            f"Historical average: "
            f"{historical_average:.2f}"
        )

        print(
            f"Days with records: "
            f"{total_days}"
        )