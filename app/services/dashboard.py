class Dashboard:
    def display(self, metric):
        print("\nDASHBOARD")
        print("======================")

        print(f"Metric: {metric.name}")
        print(f"Entries: {metric.entries}")
        print(f"Average: {metric.get_average():.2f}")

        latest = metric.entries[-1]

        print(f"Latest Value: {latest}")