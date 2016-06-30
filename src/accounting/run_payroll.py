from src.accounting import hourly_employee
from src.accounting import salaried_employee
import tkinter


class RunPayroll:

    def __init__(self):

        hourly_employee_process = open('../src/files/hourly_employees.csv', 'r')
        count = 0
        hourly_employee_list = {}
        EmployeeId = 0
        LastName = 1
        FirstName = 2
        HourlyRate = 3
        UnionDues = 4
        PaymentMethod = 5
        for line in hourly_employee_process:
            if count !=0:
                record = line.split(',')
                record[UnionDues] = record[UnionDues].strip()
                record[PaymentMethod] = record[PaymentMethod].strip()
                if record [UnionDues] == '-':
                    record [UnionDues] = 0
                employee = hourly_employee.HourlyEmployee(record[EmployeeId], record[LastName], record[FirstName], record[HourlyRate], record[UnionDues], record[PaymentMethod], '123 Main Street', 'Clearwater', 'FL', '33777')
                hourly_employee_list[record[EmployeeId]] = employee

            count += 1
        hourly_employee_process.close()

        time_card_process = open('../src/files/timecards.csv', 'r')
        count = 0
        for line in time_card_process:
            if count !=0:
                card = line.split(',')
                card[HourlyRate] = card[HourlyRate].strip()
                hourly_employee_list[card[EmployeeId]].clock_in(card[HourlyRate], card[LastName])
                hourly_employee_list[card[EmployeeId]].clock_out(card[HourlyRate], card[FirstName])

            count += 1
        time_card_process.close()

        for record in hourly_employee_list:
            hourly_employee_list[record].calculate_pay()

        salaried_employee_process = open('../src/files/salaried_employees.csv', 'r')
        count = 0
        salaried_employee_list = {}
        EmployeeId = 0
        LastName = 1
        FirstName = 2
        Salary = 3
        CommissionRate = 4
        UnionDues = 5
        PaymentMethod = 6
        for line in salaried_employee_process:
            if count !=0:
                record = line.split(',')
                record[UnionDues] = record[UnionDues].strip()
                record[PaymentMethod] = record[PaymentMethod].strip()
                if record [UnionDues] == '-':
                    record [UnionDues] = 0
                employee = salaried_employee.SalariedEmployee(record[EmployeeId], record[LastName], record[FirstName], record[Salary], record[CommissionRate], record[UnionDues], record[PaymentMethod], '12445 Canal Street', 'Tiere Verde', 'FL', '32796')
                salaried_employee_list[record[EmployeeId]] = employee

            count += 1

        salaried_employee_process.close()

        receipt_process = open('../src/files/receipts.csv', 'r')
        count = 0
        EmployeeId=0
        LastName=1
        Item=2
        Units=3
        Unit_Cost=4
        Total=5
        for line in receipt_process:
            if count != 0:
                comma_count = 0
                line2 = ''
                for record in range(0, len(line)):
                    if line[record] == ',':
                        comma_count += 1
                        if comma_count > 5:
                            continue
                        else:
                            line2 = line2 + ','
                    else:
                        line2 = line2 + line[record]

                receipt_data = line2.split(',')
                total = receipt_data[Total].strip()
                total = total.strip('"')
                total = total.strip()
                total_float = float(total)
                salaried_employee_list[receipt_data[EmployeeId]].make_sale(receipt_data[EmployeeId], receipt_data[LastName], receipt_data[Item], int(receipt_data[Units]), float(receipt_data[Unit_Cost]), total_float)

            count += 1
        receipt_process.close()

        for y in salaried_employee_list:
            salaried_employee_list[y].calculate_pay()