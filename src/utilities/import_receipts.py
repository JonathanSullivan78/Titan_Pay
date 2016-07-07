import sqlite3


def import_receipts():
    conn = sqlite3.connect('../src/files/system_database.sqlite')
    cursor = conn.cursor()
    receipt_processor = open('../src/files/receipts.csv', 'r')
    count = 0
    Employee_ID = 0
    Last_Name = 1
    Item = 2
    Units = 3
    Unit_Cost = 4
    Total = 5
    for line in receipt_processor:
        if count != 0:
            record = line.split(',')
            cursor.execute("INSERT INTO Receipts VALUES(?,?,?,?,?,?)",(record[Employee_ID], record[Last_Name], record[Item], record[Units], record[Unit_Cost], record[Total]))
        count += 1
    receipt_processor.close()
    conn.commit()
    conn.close()
