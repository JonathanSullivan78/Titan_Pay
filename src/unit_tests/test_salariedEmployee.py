from unittest import TestCase
from src.accounting import  salaried_employee


class TestSalariedEmployee(TestCase):
    def test_make_sale(self):
        sample_employee = salaried_employee.SalariedEmployee('86', 'Sullivan', 'Jonathan', '77676', '7', '0.00', 'MA', '123 Main Street', 'Testville', 'FL', '33777')
        sample_employee.make_sale('86', 'Sullivan', 'Stuff', '1', '125', 125)
        test_length = sample_employee.get_receipt_count()
        self.assertEqual(test_length, 1)
