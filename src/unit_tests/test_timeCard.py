from unittest import TestCase
from src.accounting import time_card

class TestTimeCard(TestCase):
    def test_get_timecard_date(self):
        sample_card = time_card.TimeCard('7/7/16', '800', '1700')
        sample_date = sample_card.get_timecard_date()
        self.assertTrue(sample_date)

    def test_calculate_daily_pay(self):
        sample_card = time_card.TimeCard('7/7/16', '800', '1700')
        sample_pay = sample_card.calculate_daily_pay('10.00')
        self.assertEqual(sample_pay, 95)


    def test_set_end_time(self):
        sample_card = time_card.TimeCard('7/7/16', '800', '')
        sample_card.set_end_time('1700')
        self.assertEqual(sample_card.end_time, '1700')
