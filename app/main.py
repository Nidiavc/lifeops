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

    study_hours.add_entry(3)
    storage.save_metric_entry(
        "Study Hours",
        3,
        today
    )

    study_hours.add_entry(5)
    storage.save_metric_entry(
        "Study Hours",
        5,
        today
    )

    study_hours.add_entry(2)
    storage.save_metric_entry(
        "Study Hours",
        2,
        today
    )

    app.add_metric(study_hours)
    storage.save_metric(study_hours)

    # -------------------------
    # SLEEP HOURS
    # -------------------------

    sleep_hours = Metric(
        "Sleep Hours",
        "Hours"
    )

    sleep_hours.add_entry(7)
    storage.save_metric_entry(
        "Sleep Hours",
        7,
        today
    )

    sleep_hours.add_entry(8)
    storage.save_metric_entry(
        "Sleep Hours",
        8,
        today
    )

    sleep_hours.add_entry(6)
    storage.save_metric_entry(
        "Sleep Hours",
        6,
        today
    )

    app.add_metric(sleep_hours)
    storage.save_metric(sleep_hours)

    # -------------------------
    # SAVINGS
    # -------------------------

    savings = Metric(
        "Savings",
        "CLP"
    )

    savings.add_entry(100000)
    storage.save_metric_entry(
        "Savings",
        100000,
        today
    )

    savings.add_entry(150000)
    storage.save_metric_entry(
        "Savings",
        150000,
        today
    )

    savings.add_entry(200000)
    storage.save_metric_entry(
        "Savings",
        200000,
        today
    )

    app.add_metric(savings)
    storage.save_metric(savings)

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
    # METRIC ENTRY
    # -------------------------

    study_entry = MetricEntry(
        "Study Hours",
        3
    )

    # -------------------------
    # OUTPUT
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

    metrics_service = MetricsService()
    dashboard = Dashboard()

    print("\nDASHBOARD")
    print("======================")

    dashboard.display(study_hours)
    dashboard.display(sleep_hours)
    dashboard.display(savings)

    print("\nMETRIC STATISTICS")
    print("======================")

    print(
        f"Study Average: "
        f"{metrics_service.calculate_average(study_hours):.2f}"
    )

    print(
        f"Sleep Average: "
        f"{metrics_service.calculate_average(sleep_hours):.2f}"
    )

    print(
        f"Savings Average: "
        f"{metrics_service.calculate_average(savings):.2f}"
    )

    print("\nDATABASE")
    print("======================")

    storage.show_metrics()

    print("\nMETRIC ENTRIES")
    print("======================")

    storage.show_metric_entries()

    print("\nGOALS")
    print("======================")

    storage.show_goals()

    print("\nGOAL STATISTICS")
    print("======================")

    print(
        f"Average Goal Progress: "
        f"{storage.get_goal_average_progress():.2f}"
    )

    print(
        f"Goal Count: "
        f"{storage.get_goal_count()}"
    )

    print(
        f"Max Goal Progress: "
        f"{storage.get_goal_max_progress()}"
    )

    print(
        f"Min Goal Progress: "
        f"{storage.get_goal_min_progress()}"
    )

    print("\nLATEST METRIC VALUE")
    print("======================")

    latest_value = storage.get_metric_latest_value(
        "Study Hours"
    )

    print(
        f"Last Recorded Study Value: {latest_value}"
    )

    print("\nSQL AVERAGE")
    print("======================")

    study_average = storage.get_metric_average(
        "Study Hours"
    )

    print(
        f"Study Average from SQLite: "
        f"{study_average:.2f}"
    )

    print("\nTODAY'S SQL AVERAGES")
    print("======================")

    study_today_average = storage.get_metric_average_by_date(
        "Study Hours",
        today
    )

    sleep_today_average = storage.get_metric_average_by_date(
        "Sleep Hours",
        today
    )

    savings_today_average = storage.get_metric_average_by_date(
        "Savings",
        today
    )

    print(
        f"Study Average Today: "
        f"{study_today_average:.2f}"
    )

    print(
        f"Sleep Average Today: "
        f"{sleep_today_average:.2f}"
    )

    print(
        f"Savings Average Today: "
        f"{savings_today_average:.2f}"
    )

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