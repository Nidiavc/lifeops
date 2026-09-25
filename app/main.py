from models.area import Area

print("=== LifeOps ===")

areas = [
    Area("Health", "Health and wellness"),
    Area("Study", "Courses and certifications"),
    Area("Finance", "Savings and expenses"),
    Area("Work", "Professional development"),
    Area("Personal", "Personal goals")
]

for area in areas:
    area.display()
    print("-------------------")