from models.area import Area
from models.metric import Metric
from models.event import Event
from models.goal import Goal
from models.metric_entry import MetricEntry


def main():
    print("=== LifeOps ===")

    areas = [
        Area("Health", "Health and wellness"),
        Area("Study", "Courses and certifications"),
        Area("Finance", "Savings and expenses"),
        Area("Work", "Professional development"),
        Area("Personal", "Personal goals"),
    ]

    print("\nAREAS")
    print("======================")

    for area in areas:
        area.display()
        print("-------------------")

    study_hours = Metric(
        "Study Hours",
        "Hours"
    )

    study_hours.add_entry(3)
    study_hours.add_entry(5)
    study_hours.add_entry(2)

    print("\nMETRIC")
    print("======================")

    study_hours.display()

    lifeops_start = Event(
        "LifeOps Started",
        "Beginning of the LifeOps project"
    )

    print("\nEVENT")
    print("======================")

    lifeops_start.display()

    power_bi_goal = Goal(
        "Get Power BI Certification",
        35
    )

    print("\nGOAL")
    print("======================")

    power_bi_goal.display()

    study_entry = MetricEntry(
        "Study Hours",
        3
    )

    print("\nMETRIC ENTRY")
    print("======================")

    study_entry.display()


if __name__ == "__main__":
    main()