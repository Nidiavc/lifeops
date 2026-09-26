class Metric:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        self.entries = []

    def add_entry(self, value):
        self.entries.append(value)

    def get_average(self):
        if len(self.entries) == 0:
            return 0

        return sum(self.entries) / len(self.entries)

    def display(self):
        print(f"Metric: {self.name}")
        print(f"Unit: {self.unit}")
        print(f"Entries: {self.entries}")
        print(f"Average: {self.get_average():.2f}")