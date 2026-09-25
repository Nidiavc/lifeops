class Metric:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def display(self):
        print(f"Metric: {self.name}")
        print(f"Unit: {self.unit}")