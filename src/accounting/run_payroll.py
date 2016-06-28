from src.accounting import hourly_employee
from src.accounting import salaried_employee


def run_payroll():

    hourly_employee_process = open('hourly_employees.csv', 'r')
    count = 0
    hourly_employee_list = {}
    for line in hourly_employee_process:
        if count !=0:
            x = line.split(',')
            x[4] = x[4].strip()
            x[5] = x[5].strip()
            if x [4] == '-':
                x [4] = 0
            employee = hourly_employee.Hourly_Employee(x[0], x[1], x[2], x[3], x[4], x[5], 'Address', 'City', 'State', 'Zip Code')
            hourly_employee_list[x[0]] = employee

        count += 1
    hourly_employee_process.close()

    time_card_process = open('timecards.csv', 'r')
    count = 0
    for line in time_card_process:
        if count !=0:
            card = line.split(',')
            card[3] = card[3].strip()
            hourly_employee_list[card[0]].clock_in(card[3], card[1])
            hourly_employee_list[card[0]].clock_out(card[3], card[2])

        count += 1
    time_card_process.close()

    for x in hourly_employee_list:
        hourly_employee_list[x].calculate_pay()

    salaried_employee_process = open('salaried_employees.csv', 'r')
    count = 0
    salaried_employee_list = {}
    for line in salaried_employee_process:
        if count !=0:
            y = line.split(',')
            y[5] = y[5].strip()
            y[6] = y[6].strip()
            if y[5] == '-':
                y[5] = 0
            employee = salaried_employee.SalariedEmployee(y[0], y[1], y[2], y[3], y[4], y[5], y[6], 'Address', 'City', 'State', 'Zip Code')
            salaried_employee_list[y[0]] = employee

        count += 1

    salaried_employee_process.close()

    receipt_process = open('receipts.csv', 'r')
    count = 0
    for line in receipt_process:
        if count != 0:
            comma_count = 0
            line2 = ''
            for z in range(0, len(line)):
                if line[z] == ',':
                    comma_count += 1
                    if comma_count > 5:
                        continue
                    else:
                        line2 = line2 + ','
                else:
                    line2 = line2 + line[z]

            receipt_data = line2.split(',')
            total = receipt_data[5].strip()
            total = total.strip('"')
            total = total.strip()
            total_float = float(total)
            salaried_employee_list[receipt_data[0]].make_sale(receipt_data[0], receipt_data[1], receipt_data[2], int(receipt_data[3]), float(receipt_data[4]), total_float)

        count += 1
    receipt_process.close()

    for y in salaried_employee_list:
        salaried_employee_list[y].calculate_pay()
