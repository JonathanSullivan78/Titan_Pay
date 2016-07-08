from src.accounting import hourly_employee
from src.accounting import salaried_employee
import sqlite3


class RunPayroll:

    def __init__(self):

        # Hourly Employee Processor
        con = sqlite3.connect('../src/files/system_database.sqlite')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Hourly_Employees WHERE Employee_ID')
        hourly_employee_processor = cursor.fetchall()
        hourly_employee_list = {}

        EmployeeId = 0
        LastName = 1
        FirstName = 2
        HourlyRate = 3
        UnionDues = 4
        PaymentMethod = 5

        for record in hourly_employee_processor:
            employee = hourly_employee.HourlyEmployee(record[EmployeeId], record[LastName], record[FirstName],
                                                      record[HourlyRate], record[UnionDues], record[PaymentMethod],
                                                      '123 Main Street', 'Clearwater', 'FL', '33777')
            hourly_employee_list[record[EmployeeId]] = employee
        con.close()
        
        # Time Card Processor
        con = sqlite3.connect('../src/files/system_database.sqlite')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Time_Cards WHERE Employee_ID')
        time_card_processor = cursor.fetchall()
        for record in time_card_processor:
                hourly_employee_list[record[EmployeeId]].clock_in(record[HourlyRate], record[LastName])
                hourly_employee_list[record[EmployeeId]].clock_out(record[HourlyRate], record[FirstName])
        con.close()

        for record in hourly_employee_list:
           hourly_employee_list[record].calculate_pay()


        # Salaried Employee Processor
        con = sqlite3.connect('../src/files/system_database.sqlite')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Salaried_Employees WHERE Employee_ID')
        salaried_employee_processor = cursor.fetchall()
        salaried_employee_list = {}

        EmployeeId = 0
        LastName = 1
        FirstName = 2
        Salary = 3
        CommissionRate = 4
        UnionDues = 5
        PaymentMethod = 6

        for record in salaried_employee_processor:
            employee = salaried_employee.SalariedEmployee(record[EmployeeId], record[LastName], record[FirstName],
                                                          record[Salary], record[CommissionRate], record[UnionDues],
                                                          record[PaymentMethod], '12445 Canal Street', 'Tiere Verde',
                                                          'FL', '32796')
            salaried_employee_list[record[EmployeeId]] = employee
        con.close()

        # Receipt Processor
        con = sqlite3.connect('../src/files/system_database.sqlite')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Receipts WHERE Employee_ID')
        receipt_processor = cursor.fetchall()

        EmployeeId = 0
        LastName = 1
        Item = 2
        Units = 3
        Unit_Cost = 4
        Total = 5

        for record in receipt_processor:
            salaried_employee_list[record[EmployeeId]].make_sale(record[EmployeeId], record[LastName],
                                                                 record[Item], int(record[Units]),
                                                                 float(record[Unit_Cost]), record[Total])
        con.close()

        for record in salaried_employee_list:
            salaried_employee_list[record].calculate_pay()