from datetime import date


class WeeklyAnalyticsService:
    def get_weekly_averages(self, history):
        weekly_values = {}

        for entry_date, average_value in history:
            parsed_date = date.fromisoformat(
                entry_date
            )

            iso_year, iso_week, _ = (
                parsed_date.isocalendar()
            )

            week_key = (
                f"{iso_year}-W{iso_week:02d}"
            )

            if week_key not in weekly_values:
                weekly_values[week_key] = []

            weekly_values[week_key].append(
                average_value
            )

        weekly_averages = []

        for week_key in sorted(
            weekly_values.keys()
        ):
            values = weekly_values[week_key]

            average = sum(values) / len(values)

            weekly_averages.append(
                (
                    week_key,
                    average
                )
            )

        return weekly_averages

    def get_highest_week(
        self,
        weekly_averages
    ):
        if not weekly_averages:
            return None

        return max(
            weekly_averages,
            key=lambda record: record[1]
        )

    def get_lowest_week(
        self,
        weekly_averages
    ):
        if not weekly_averages:
            return None

        return min(
            weekly_averages,
            key=lambda record: record[1]
        )

    def get_weekly_growth(
        self,
        weekly_averages
    ):
        if len(weekly_averages) < 2:
            return 0

        previous_average = (
            weekly_averages[-2][1]
        )

        latest_average = (
            weekly_averages[-1][1]
        )

        if previous_average == 0:
            return 0

        difference = (
            latest_average - previous_average
        )

        return (
            difference / previous_average
        ) * 100

    def get_weekly_trend(
        self,
        weekly_averages
    ):
        if len(weekly_averages) < 2:
            return "Insufficient data"

        previous_average = (
            weekly_averages[-2][1]
        )

        latest_average = (
            weekly_averages[-1][1]
        )

        if latest_average > previous_average:
            return "Increasing"

        if latest_average < previous_average:
            return "Decreasing"

        return "Stable"

    def display(
        self,
        metric_name,
        history
    ):
        print(
            f"\n{metric_name.upper()} "
            "WEEKLY ANALYTICS"
        )

        print("======================")

        weekly_averages = (
            self.get_weekly_averages(
                history
            )
        )

        if not weekly_averages:
            print(
                "No dated records available "
                "for weekly analytics."
            )
            return

        for week_key, average in (
            weekly_averages
        ):
            print(
                f"{week_key} -> "
                f"{average:.2f}"
            )

        highest_week = (
            self.get_highest_week(
                weekly_averages
            )
        )

        lowest_week = (
            self.get_lowest_week(
                weekly_averages
            )
        )

        print(
            "\nHighest weekly average:"
        )

        print(
            f"{highest_week[0]} -> "
            f"{highest_week[1]:.2f}"
        )

        print(
            "\nLowest weekly average:"
        )

        print(
            f"{lowest_week[0]} -> "
            f"{lowest_week[1]:.2f}"
        )

        weekly_growth = (
            self.get_weekly_growth(
                weekly_averages
            )
        )

        weekly_trend = (
            self.get_weekly_trend(
                weekly_averages
            )
        )

        print(
            f"\nWeekly growth: "
            f"{weekly_growth:.2f}%"
        )

        print(
            f"Weekly trend: "
            f"{weekly_trend}"
        )