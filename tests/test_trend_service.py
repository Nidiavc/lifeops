import unittest

from app.services.trend_service import TrendService


class TestTrendService(unittest.TestCase):

    def setUp(self):
        self.service = TrendService()

    def test_increasing_trend(self):
        history = [
            ("2026-09-30", 2.67),
            ("2026-10-01", 3.33),
        ]

        result = self.service.calculate_trend(
            history
        )

        self.assertEqual(
            result,
            "Increasing"
        )

    def test_decreasing_trend(self):
        history = [
            ("2026-09-30", 8.00),
            ("2026-10-01", 7.00),
        ]

        result = self.service.calculate_trend(
            history
        )

        self.assertEqual(
            result,
            "Decreasing"
        )

    def test_stable_trend(self):
        history = [
            ("2026-09-30", 7.00),
            ("2026-10-01", 7.00),
        ]

        result = self.service.calculate_trend(
            history
        )

        self.assertEqual(
            result,
            "Stable"
        )

    def test_insufficient_data(self):
        history = [
            ("2026-10-01", 3.33),
        ]

        result = self.service.calculate_trend(
            history
        )

        self.assertEqual(
            result,
            "Insufficient data"
        )

    def test_absolute_change(self):
        history = [
            ("2026-09-30", 100000),
            ("2026-10-01", 150000),
        ]

        result = self.service.get_change(
            history
        )

        self.assertEqual(
            result,
            50000
        )

    def test_percentage_change(self):
        history = [
            ("2026-09-30", 100000),
            ("2026-10-01", 150000),
        ]

        result = (
            self.service.get_percentage_change(
                history
            )
        )

        self.assertAlmostEqual(
            result,
            50.00,
            places=2
        )

    def test_percentage_change_with_zero(self):
        history = [
            ("2026-09-30", 0),
            ("2026-10-01", 100),
        ]

        result = (
            self.service.get_percentage_change(
                history
            )
        )

        self.assertEqual(
            result,
            0
        )


if __name__ == "__main__":
    unittest.main()