import unittest

from app.services.insights_service import InsightsService


class TestInsightsService(unittest.TestCase):

    def setUp(self):
        self.service = InsightsService()

    def test_highest_day(self):
        history = [
            ("2026-09-30", 2.67),
            ("2026-10-01", 3.33),
        ]

        result = self.service.get_highest_day(
            history
        )

        self.assertEqual(
            result,
            ("2026-10-01", 3.33)
        )

    def test_lowest_day(self):
        history = [
            ("2026-09-30", 2.67),
            ("2026-10-01", 3.33),
        ]

        result = self.service.get_lowest_day(
            history
        )

        self.assertEqual(
            result,
            ("2026-09-30", 2.67)
        )

    def test_historical_average(self):
        history = [
            ("2026-09-30", 100000),
            ("2026-10-01", 150000),
        ]

        result = (
            self.service.get_historical_average(
                history
            )
        )

        self.assertEqual(
            result,
            125000
        )

    def test_total_days(self):
        history = [
            ("2026-09-30", 100000),
            ("2026-10-01", 150000),
        ]

        result = self.service.get_total_days(
            history
        )

        self.assertEqual(
            result,
            2
        )

    def test_empty_history(self):
        history = []

        highest = self.service.get_highest_day(
            history
        )

        lowest = self.service.get_lowest_day(
            history
        )

        average = (
            self.service.get_historical_average(
                history
            )
        )

        count = self.service.get_total_days(
            history
        )

        self.assertIsNone(highest)
        self.assertIsNone(lowest)
        self.assertEqual(average, 0)
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()