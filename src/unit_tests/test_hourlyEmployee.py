from unittest import TestCase
from src.accounting import hourly_employee


class TestHourlyEmployee(TestCase):
    def test_clock_in(self):
        sample_employee = hourly_employee.HourlyEmployee('86', 'Sullivan', 'Jonathan', '19.95', '0.00', 'MA',
                                                          '123 Main Street', 'Testville', 'FL', '33777')
        sample_employee.clock_in('7/4/2016', '0800')
        test_length = sample_employee.get_timecard_length()
        self.assertEqual(test_length, 1)

    def test_clock_out(self):
        sample_employee = hourly_employee.HourlyEmployee('86', 'Sullivan', 'Jonathan', '19.95', '0.00', 'MA',
                                                         '123 Main Street', 'Testville', 'FL', '33777')

        sample_employee.clock_in('7/4/2016', '0800')
        sample_employee.clock_out('7/4/2016', '1700')
        test_time = sample_employee.get_timecard_end_time()
        self.assertEqual(test_time, '1700')

    def test_calculate_pay(self):
        sample_employee = hourly_employee.HourlyEmployee('86', 'Sullivan', 'Jonathan', '19.95', '0.00', 'MA',
                                                         '123 Main Street', 'Testville', 'FL', '33777')
        sample_employee.clock_in('7/4/2016', '0800')
        sample_employee.clock_out('7/4/2016', '1700')
        test_pay = sample_employee.calculate_pay()
        self.assertEqual(format(test_pay,'.2f'), '189.52')
