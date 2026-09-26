class MetricEntry:
    def __init__(self, metric_name, value):
        self.metric_name = metric_name
        self.value = value

    def display(self):
        print(f"Metric: {self.metric_name}")
        print(f"Value: {self.value}")