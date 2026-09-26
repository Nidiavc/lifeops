from models.area import Area
from models.metric import Metric
from models.event import Event
from models.goal import Goal
from models.metric_entry import MetricEntry

from services.dashboard import Dashboard
from services.lifeops_app import LifeOpsApp

from database.storage import Storage


def main():
    print("=== LifeOps ===")

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

    study_hours = Metric(
        "Study Hours",
        "Hours"
    )

    study_hours.add_entry(3)
    study_hours.add_entry(5)
    study_hours.add_entry(2)

    app.add_metric(study_hours)

    storage.save_metric(study_hours)

    lifeops_start = Event(
        "LifeOps Started",
        "Beginning of the LifeOps project"
    )

    app.add_event(lifeops_start)

    power_bi_goal = Goal(
        "Get Power BI Certification",
        35
    )

    app.add_goal(power_bi_goal)

    study_entry = MetricEntry(
        "Study Hours",
        3
    )

    print("\nAREAS")
    print("======================")

    for area in app.areas:
        area.display()
        print("-------------------")

    print("\nMETRIC")
    print("======================")

    study_hours.display()

    print("\nEVENT")
    print("======================")

    lifeops_start.display()

    print("\nGOAL")
    print("======================")

    power_bi_goal.display()

    print("\nMETRIC ENTRY")
    print("======================")

    study_entry.display()

    dashboard = Dashboard()

    dashboard.display(study_hours)

    print("\nDATABASE")
    print("======================")

    storage.show_metrics()

    app.summary()


if __name__ == "__main__":
    main()