from datetime import date

from models.area import Area
from models.metric import Metric
from models.event import Event
from models.goal import Goal
from models.metric_entry import MetricEntry

from services.dashboard import Dashboard
from services.summary_dashboard import SummaryDashboard
from services.lifeops_app import LifeOpsApp
from services.metrics_service import MetricsService

from database.storage import Storage


def display_metric_history(
    storage,
    metric_name
):
    print(f"\n{metric_name.upper()} HISTORY")
    print("======================")

    history = storage.get_metric_history(
        metric_name
    )

    if not history:
        print("No dated records available.")
        return

    for entry_date, average_value in history:
        print(
            f"{entry_date} -> "
            f"{average_value:.2f}"
        )


def main():
    print("=== LifeOps ===")

    today = date.today().isoformat()

    storage = Storage()
    storage.create_tables()

    app = LifeOpsApp()

    areas = [
        Area("Health", "Health and wellness"),
        Area("Study", "Courses and certifications"),
        Area("Finance", "Savings and expenses"),
        Area("Work", "Professional development"),
        Area("Personal", "Personal goals"),
    ]

    for area in areas:
        app.add_area(area)

    # -------------------------
    # STUDY HOURS
    # -------------------------

    study_hours = Metric(
        "Study Hours",
        "Hours"
    )

    app.add_metric(study_hours)
    storage.save_metric(study_hours)

    study_values = [3, 5, 2]

    for value in study_values:
        study_hours.add_entry(value)

        storage.save_metric_entry(
            "Study Hours",
            value,
            today
        )

    # -------------------------
    # SLEEP HOURS
    # -------------------------

    sleep_hours = Metric(
        "Sleep Hours",
        "Hours"
    )

    app.add_metric(sleep_hours)
    storage.save_metric(sleep_hours)

    sleep_values = [7, 8, 6]

    for value in sleep_values:
        sleep_hours.add_entry(value)

        storage.save_metric_entry(
            "Sleep Hours",
            value,
            today
        )

    # -------------------------
    # SAVINGS
    # -------------------------

    savings = Metric(
        "Savings",
        "CLP"
    )

    app.add_metric(savings)
    storage.save_metric(savings)

    savings_values = [
        100000,
        150000,
        200000
    ]

    for value in savings_values:
        savings.add_entry(value)

        storage.save_metric_entry(
            "Savings",
            value,
            today
        )

    # -------------------------
    # EVENT
    # -------------------------

    lifeops_start = Event(
        "LifeOps Started",
        "Beginning of the LifeOps project"
    )

    app.add_event(lifeops_start)

    # -------------------------
    # GOAL
    # -------------------------

    power_bi_goal = Goal(
        "Get Power BI Certification",
        35
    )

    app.add_goal(power_bi_goal)
    storage.save_goal(power_bi_goal)

    # -------------------------
    # METRIC ENTRY EXAMPLE
    # -------------------------

    study_entry = MetricEntry(
        "Study Hours",
        3
    )

    # -------------------------
    # GENERAL OUTPUT
    # -------------------------

    print(f"\nEntry date: {today}")

    print("\nAREAS")
    print("======================")

    for area in app.areas:
        area.display()
        print("-------------------")

    print("\nMETRICS")
    print("======================")

    study_hours.display()
    print()

    sleep_hours.display()
    print()

    savings.display()

    print("\nEVENT")
    print("======================")

    lifeops_start.display()

    print("\nGOAL")
    print("======================")

    power_bi_goal.display()

    print("\nMETRIC ENTRY")
    print("======================")

    study_entry.display()

    # -------------------------
    # SERVICES
    # -------------------------

    metrics_service = MetricsService()
    dashboard = Dashboard()

    # -------------------------
    # DASHBOARDS
    # -------------------------

    print("\nDASHBOARDS")
    print("======================")

    dashboard.display(study_hours)
    dashboard.display(sleep_hours)
    dashboard.display(savings)

    # -------------------------
    # MEMORY STATISTICS
    # -------------------------

    print("\nMETRIC STATISTICS")
    print("======================")

    print(
        "Study Average: "
        f"{metrics_service.calculate_average(study_hours):.2f}"
    )

    print(
        "Sleep Average: "
        f"{metrics_service.calculate_average(sleep_hours):.2f}"
    )

    print(
        "Savings Average: "
        f"{metrics_service.calculate_average(savings):.2f}"
    )

    # -------------------------
    # DATABASE DATA
    # -------------------------

    print("\nDATABASE METRICS")
    print("======================")

    storage.show_metrics()

    print("\nDATABASE METRIC ENTRIES")
    print("======================")

    storage.show_metric_entries()

    print("\nDATABASE GOALS")
    print("======================")

    storage.show_goals()

    # -------------------------
    # GOAL STATISTICS
    # -------------------------

    print("\nGOAL STATISTICS")
    print("======================")

    print(
        "Average Goal Progress: "
        f"{storage.get_goal_average_progress():.2f}"
    )

    print(
        "Goal Count: "
        f"{storage.get_goal_count()}"
    )

    print(
        "Max Goal Progress: "
        f"{storage.get_goal_max_progress()}"
    )

    print(
        "Min Goal Progress: "
        f"{storage.get_goal_min_progress()}"
    )

    # -------------------------
    # LATEST VALUE
    # -------------------------

    print("\nLATEST METRIC VALUES")
    print("======================")

    print(
        "Latest Study Value: "
        f"{storage.get_metric_latest_value('Study Hours')}"
    )

    print(
        "Latest Sleep Value: "
        f"{storage.get_metric_latest_value('Sleep Hours')}"
    )

    print(
        "Latest Savings Value: "
        f"{storage.get_metric_latest_value('Savings')}"
    )

    # -------------------------
    # SQL AVERAGES
    # -------------------------

    print("\nSQL AVERAGES")
    print("======================")

    print(
        "Study Average from SQLite: "
        f"{storage.get_metric_average('Study Hours'):.2f}"
    )

    print(
        "Sleep Average from SQLite: "
        f"{storage.get_metric_average('Sleep Hours'):.2f}"
    )

    print(
        "Savings Average from SQLite: "
        f"{storage.get_metric_average('Savings'):.2f}"
    )

    # -------------------------
    # TODAY'S SQL AVERAGES
    # -------------------------

    print("\nTODAY'S SQL AVERAGES")
    print("======================")

    print(
        "Study Average Today: "
        f"{storage.get_metric_average_by_date('Study Hours', today):.2f}"
    )

    print(
        "Sleep Average Today: "
        f"{storage.get_metric_average_by_date('Sleep Hours', today):.2f}"
    )

    print(
        "Savings Average Today: "
        f"{storage.get_metric_average_by_date('Savings', today):.2f}"
    )

    # -------------------------
    # TEMPORAL HISTORY
    # -------------------------

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

    # -------------------------
    # SUMMARY DASHBOARD
    # -------------------------

    summary_dashboard = SummaryDashboard()

    summary_dashboard.display(
        metrics_service.calculate_average(
            study_hours
        ),
        metrics_service.calculate_average(
            sleep_hours
        ),
        metrics_service.calculate_average(
            savings
        ),
        storage.get_goal_count(),
        storage.get_metric_latest_value(
            "Study Hours"
        )
    )

    app.summary()
    storage.close()


if __name__ == "__main__":
    main()