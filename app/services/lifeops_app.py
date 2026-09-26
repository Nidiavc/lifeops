class LifeOpsApp:
    def __init__(self):
        self.areas = []
        self.metrics = []
        self.events = []
        self.goals = []

    def add_area(self, area):
        self.areas.append(area)

    def add_metric(self, metric):
        self.metrics.append(metric)

    def add_event(self, event):
        self.events.append(event)

    def add_goal(self, goal):
        self.goals.append(goal)

    def summary(self):
        print("\nLIFEOPS SUMMARY")
        print("======================")
        print(f"Areas: {len(self.areas)}")
        print(f"Metrics: {len(self.metrics)}")
        print(f"Events: {len(self.events)}")
        print(f"Goals: {len(self.goals)}")