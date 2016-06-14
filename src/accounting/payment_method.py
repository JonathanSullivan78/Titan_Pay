from src.accounting.address import Address
from src.accounting.employee import Employee
from src.accounting.hourly_employee import Hourly_Employee
from src.accounting.salaried_employee import SalariedEmployee

class PaymentMethod(Address, Employee, Hourly_Employee, SalariedEmployee):
    def __init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay):
        Employee.__init__(self, first_name, last_name)
        Address.__init__(self, street_address, city, state, zip_code)
        Hourly_Employee.__init__(self, total_pay)
        SalariedEmployee.__init__(self, total_pay)