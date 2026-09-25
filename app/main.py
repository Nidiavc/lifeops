from models.area import Area
from models.metric import Metric
from models.event import Event

print("=== LifeOps ===")

# Areas
areas = [
    Area("Health", "Health and wellness"),
    Area("Study", "Courses and certifications"),
    Area("Finance", "Savings and expenses"),
    Area("Work", "Professional development"),
    Area("Personal", "Personal goals")
]

print("\nAREAS")
print("======================")

for area in areas:
    area.display()
    print("-------------------")

# Metric
study_hours = Metric(
    "Study Hours",
    "Hours"
)

print("\nMETRIC")
print("======================")

study_hours.display()

# Event
lifeops_start = Event(
    "LifeOps Started",
    "Beginning of the LifeOps project"
)

print("\nEVENT")
print("======================")

lifeops_start.display()