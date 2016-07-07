import sqlite3


def import_employees():
    conn = sqlite3.connect('../src/files/system_database.sqlite')
    cursor = conn.cursor()
    hourly_employee_processor = open('../src/files/hourly_employees.csv', 'r')
    count = 0
    Employee_ID = 0
    Last_Name = 1
    First_Name = 2
    HourlyRate = 3
    Union_Dues = 4
    Payment_Method = 5
    for line in hourly_employee_processor:
        if count != 0:
            record = line.split(',')
            record[Union_Dues] = record[Union_Dues].strip()
            record[Payment_Method] = record[Payment_Method].strip()
            if record[Union_Dues] == '-':
                record[Union_Dues] = 0
            cursor.execute("INSERT INTO Hourly_Employees VALUES (?,?,?,?,?,?)", (record[Employee_ID], record[Last_Name], record[First_Name], record[HourlyRate], record[Union_Dues], record[Payment_Method]))
        count += 1
    hourly_employee_processor.close()
    salaried_employee_processor = open('../src/files/salaried_employees.csv', 'r')
    count = 0
    Employee_ID = 0
    Last_Name = 1
    First_Name = 2
    Salary_Rate = 3
    Commission_Rate = 4
    Union_Dues = 5
    Payment_Method = 6
    for line in salaried_employee_processor:
        if count != 0:
            record = line.split(',')
            record[Union_Dues] = record[Union_Dues].strip()
            record[Payment_Method] = record[Payment_Method].strip()
            if record[Union_Dues] == '-':
                record[Union_Dues] = 0
            cursor.execute("INSERT INTO Salaried_Employees VALUES(?,?,?,?,?,?,?)",
                           (record[Employee_ID], record[Last_Name], record[First_Name], record[Salary_Rate], record[Commission_Rate], record[Union_Dues], record[Payment_Method]))
        count += 1

    salaried_employee_processor.close()

    conn.commit()
    conn.close()
