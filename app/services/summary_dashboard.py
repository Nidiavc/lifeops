class SummaryDashboard:

    def display(
        self,
        study_average,
        sleep_average,
        goal_count,
        latest_value
    ):

        print("\nLIFEOPS DASHBOARD SUMMARY")
        print("=========================")

        print(
            f"Study Hours Average..... {study_average:.2f}"
        )

        print(
            f"Sleep Hours Average..... {sleep_average:.2f}"
        )

        print(
            f"Goals................... {goal_count}"
        )

        print(
            f"Latest Study Value...... {latest_value}"
        )