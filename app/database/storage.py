class Storage:
    def save_metric(self, metric):
        print("\nSAVING METRIC")
        print("======================")
        print(f"Metric saved: {metric.name}")

    def load_metrics(self):
        print("\nLOADING METRICS")
        print("======================")
        return []