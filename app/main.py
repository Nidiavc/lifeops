from datetime import date
from datetime import timedelta

from models.area import Area
from models.metric import Metric
from models.event import Event
from models.goal import Goal
from models.metric_entry import MetricEntry

from services.dashboard import Dashboard
from services.summary_dashboard import SummaryDashboard
from services.lifeops_app import LifeOpsApp
from services.metrics_service import MetricsService
from services.trend_service import TrendService
from services.insights_service import InsightsService
from services.weekly_analytics_service import WeeklyAnalyticsService

from database.storage import Storage


def display_metric_history(
    storage,
    metric_name
):
    print(
        f"\n{metric_name.upper()} HISTORY"
    )
    print("======================")

    history = storage.get_metric_history(
        metric_name
    )

    if not history:
        print(
            "No dated records available."
        )
        return

    for entry_date, average_value in history:
        print(
            f"{entry_date} -> "
            f"{average_value:.2f}"
        )


def save_metric_values(
    storage,
    metric,
    values,
    entry_date,
    add_to_memory=True
):
    for value in values:
        if add_to_memory:
            metric.add_entry(value)

        storage.save_metric_entry(
            metric.name,
            value,
            entry_date
        )


def main():
    print("=== LifeOps ===")

    today = date.today()

    previous_day = today - timedelta(
        days=1
    )

    today_text = today.isoformat()

    previous_day_text = (
        previous_day.isoformat()
    )

    storage = Storage()

    try:
        storage.create_tables()

        app = LifeOpsApp()

        # ==========================
        # AREAS
        # ==========================

        areas = [
            Area(
                "Health",
                "Health and wellness"
            ),
            Area(
                "Study",
                "Courses and certifications"
            ),
            Area(
                "Finance",
                "Savings and expenses"
            ),
            Area(
                "Work",
                "Professional development"
            ),
            Area(
                "Personal",
                "Personal goals"
            ),
        ]

        for area in areas:
            app.add_area(area)

        # ==========================
        # STUDY HOURS
        # ==========================

        study_hours = Metric(
            "Study Hours",
            "Hours"
        )

        app.add_metric(study_hours)
        storage.save_metric(study_hours)

        previous_study_values = [
            2,
            3,
            3
        ]

        today_study_values = [
            3,
            5,
            2
        ]

        save_metric_values(
            storage,
            study_hours,
            previous_study_values,
            previous_day_text,
            add_to_memory=False
        )

        save_metric_values(
            storage,
            study_hours,
            today_study_values,
            today_text,
            add_to_memory=True
        )

        # ==========================
        # SLEEP HOURS
        # ==========================

        sleep_hours = Metric(
            "Sleep Hours",
            "Hours"
        )

        app.add_metric(sleep_hours)
        storage.save_metric(sleep_hours)

        previous_sleep_values = [
            6,
            7,
            7
        ]

        today_sleep_values = [
            7,
            8,
            6
        ]

        save_metric_values(
            storage,
            sleep_hours,
            previous_sleep_values,
            previous_day_text,
            add_to_memory=False
        )

        save_metric_values(
            storage,
            sleep_hours,
            today_sleep_values,
            today_text,
            add_to_memory=True
        )

        # ==========================
        # SAVINGS
        # ==========================

        savings = Metric(
            "Savings",
            "CLP"
        )

        app.add_metric(savings)
        storage.save_metric(savings)

        previous_savings_values = [
            80000,
            100000,
            120000
        ]

        today_savings_values = [
            100000,
            150000,
            200000
        ]

        save_metric_values(
            storage,
            savings,
            previous_savings_values,
            previous_day_text,
            add_to_memory=False
        )

        save_metric_values(
            storage,
            savings,
            today_savings_values,
            today_text,
            add_to_memory=True
        )

        # ==========================
        # EVENT
        # ==========================

        lifeops_start = Event(
            "LifeOps Started",
            "Beginning of the LifeOps project"
        )

        app.add_event(lifeops_start)

        # ==========================
        # GOAL
        # ==========================

        power_bi_goal = Goal(
            "Get Power BI Certification",
            35
        )

        app.add_goal(power_bi_goal)
        storage.save_goal(power_bi_goal)

        # ==========================
        # METRIC ENTRY EXAMPLE
        # ==========================

        study_entry = MetricEntry(
            "Study Hours",
            3
        )

        # ==========================
        # SERVICES
        # ==========================

        metrics_service = MetricsService()
        trend_service = TrendService()
        insights_service = InsightsService()

        weekly_analytics_service = (
            WeeklyAnalyticsService()
        )

        dashboard = Dashboard()

        # ==========================
        # GENERAL INFORMATION
        # ==========================

        print(
            "\nPrevious date: "
            f"{previous_day_text}"
        )

        print(
            "Current date: "
            f"{today_text}"
        )

        # ==========================
        # AREAS OUTPUT
        # ==========================

        print("\nAREAS")
        print("======================")

        for area in app.areas:
            area.display()
            print("-------------------")

        # ==========================
        # METRICS OUTPUT
        # ==========================

        print("\nMETRICS")
        print("======================")

        study_hours.display()
        print()

        sleep_hours.display()
        print()

        savings.display()

        # ==========================
        # EVENT OUTPUT
        # ==========================

        print("\nEVENT")
        print("======================")

        lifeops_start.display()

        # ==========================
        # GOAL OUTPUT
        # ==========================

        print("\nGOAL")
        print("======================")

        power_bi_goal.display()

        # ==========================
        # METRIC ENTRY OUTPUT
        # ==========================

        print("\nMETRIC ENTRY")
        print("======================")

        study_entry.display()

        # ==========================
        # DASHBOARDS
        # ==========================

        print("\nDASHBOARDS")
        print("======================")

        dashboard.display(
            study_hours
        )

        dashboard.display(
            sleep_hours
        )

        dashboard.display(
            savings
        )

        # ==========================
        # MEMORY STATISTICS
        # ==========================

        print("\nMETRIC STATISTICS")
        print("======================")

        study_memory_average = (
            metrics_service.calculate_average(
                study_hours
            )
        )

        sleep_memory_average = (
            metrics_service.calculate_average(
                sleep_hours
            )
        )

        savings_memory_average = (
            metrics_service.calculate_average(
                savings
            )
        )

        print(
            "Study Average: "
            f"{study_memory_average:.2f}"
        )

        print(
            "Sleep Average: "
            f"{sleep_memory_average:.2f}"
        )

        print(
            "Savings Average: "
            f"{savings_memory_average:.2f}"
        )

        # ==========================
        # DATABASE DATA
        # ==========================

        print("\nDATABASE METRICS")
        print("======================")

        storage.show_metrics()

        print("\nDATABASE METRIC ENTRIES")
        print("======================")

        storage.show_metric_entries()

        print("\nDATABASE GOALS")
        print("======================")

        storage.show_goals()

        # ==========================
        # GOAL STATISTICS
        # ==========================

        print("\nGOAL STATISTICS")
        print("======================")

        goal_average = (
            storage.get_goal_average_progress()
        )

        goal_count = (
            storage.get_goal_count()
        )

        goal_maximum = (
            storage.get_goal_max_progress()
        )

        goal_minimum = (
            storage.get_goal_min_progress()
        )

        print(
            "Average Goal Progress: "
            f"{goal_average:.2f}"
        )

        print(
            "Goal Count: "
            f"{goal_count}"
        )

        print(
            "Max Goal Progress: "
            f"{goal_maximum}"
        )

        print(
            "Min Goal Progress: "
            f"{goal_minimum}"
        )

        # ==========================
        # LATEST VALUES
        # ==========================

        print("\nLATEST METRIC VALUES")
        print("======================")

        latest_study_value = (
            storage.get_metric_latest_value(
                "Study Hours"
            )
        )

        latest_sleep_value = (
            storage.get_metric_latest_value(
                "Sleep Hours"
            )
        )

        latest_savings_value = (
            storage.get_metric_latest_value(
                "Savings"
            )
        )

        print(
            "Latest Study Value: "
            f"{latest_study_value}"
        )

        print(
            "Latest Sleep Value: "
            f"{latest_sleep_value}"
        )

        print(
            "Latest Savings Value: "
            f"{latest_savings_value}"
        )

        # ==========================
        # SQL AVERAGES
        # ==========================

        print("\nSQL AVERAGES")
        print("======================")

        study_sql_average = (
            storage.get_metric_average(
                "Study Hours"
            )
        )

        sleep_sql_average = (
            storage.get_metric_average(
                "Sleep Hours"
            )
        )

        savings_sql_average = (
            storage.get_metric_average(
                "Savings"
            )
        )

        print(
            "Study Average from SQLite: "
            f"{study_sql_average:.2f}"
        )

        print(
            "Sleep Average from SQLite: "
            f"{sleep_sql_average:.2f}"
        )

        print(
            "Savings Average from SQLite: "
            f"{savings_sql_average:.2f}"
        )

        # ==========================
        # TODAY'S SQL AVERAGES
        # ==========================

        print("\nTODAY'S SQL AVERAGES")
        print("======================")

        study_today_average = (
            storage.get_metric_average_by_date(
                "Study Hours",
                today_text
            )
        )

        sleep_today_average = (
            storage.get_metric_average_by_date(
                "Sleep Hours",
                today_text
            )
        )

        savings_today_average = (
            storage.get_metric_average_by_date(
                "Savings",
                today_text
            )
        )

        print(
            "Study Average Today: "
            f"{study_today_average:.2f}"
        )

        print(
            "Sleep Average Today: "
            f"{sleep_today_average:.2f}"
        )

        print(
            "Savings Average Today: "
            f"{savings_today_average:.2f}"
        )

        # ==========================
        # HISTORICAL DATA
        # ==========================

        study_history = (
            storage.get_metric_history(
                "Study Hours"
            )
        )

        sleep_history = (
            storage.get_metric_history(
                "Sleep Hours"
            )
        )

        savings_history = (
            storage.get_metric_history(
                "Savings"
            )
        )

        # ==========================
        # TEMPORAL HISTORY
        # ==========================

        print("\nMETRIC HISTORY")
        print("======================")

        display_metric_history(
            storage,
            "Study Hours"
        )

        display_metric_history(
            storage,
            "Sleep Hours"
        )

        display_metric_history(
            storage,
            "Savings"
        )

        # ==========================
        # TRENDS
        # ==========================

        print("\nMETRIC TRENDS")
        print("======================")

        trend_service.display(
            "Study Hours",
            study_history
        )

        trend_service.display(
            "Sleep Hours",
            sleep_history
        )

        trend_service.display(
            "Savings",
            savings_history
        )

        # ==========================
        # INSIGHTS
        # ==========================

        print("\nMETRIC INSIGHTS")
        print("======================")

        insights_service.display(
            "Study Hours",
            study_history
        )

        insights_service.display(
            "Sleep Hours",
            sleep_history
        )

        insights_service.display(
            "Savings",
            savings_history
        )

        # ==========================
        # WEEKLY ANALYTICS
        # ==========================

        print("\nWEEKLY ANALYTICS")
        print("======================")

        weekly_analytics_service.display(
            "Study Hours",
            study_history
        )

        weekly_analytics_service.display(
            "Sleep Hours",
            sleep_history
        )

        weekly_analytics_service.display(
            "Savings",
            savings_history
        )

        # ==========================
        # SUMMARY DASHBOARD
        # ==========================

        summary_dashboard = (
            SummaryDashboard()
        )

        summary_dashboard.display(
            study_memory_average,
            sleep_memory_average,
            savings_memory_average,
            goal_count,
            latest_study_value
        )

        # ==========================
        # APPLICATION SUMMARY
        # ==========================

        app.summary()

    finally:
        storage.close()


if __name__ == "__main__":
    main()