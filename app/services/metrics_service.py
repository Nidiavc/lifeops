class MetricsService:

    def add_entry(self, metric, value):
        metric.add_entry(value)

    def calculate_average(self, metric):
        return metric.get_average()

    def get_max(self, metric):
        return max(metric.entries)

    def get_min(self, metric):
        return min(metric.entries)

    def get_count(self, metric):
        return len(metric.entries)