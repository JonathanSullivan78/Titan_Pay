from src.accounting.employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__salary = 0
        self.__commission_rate = 0