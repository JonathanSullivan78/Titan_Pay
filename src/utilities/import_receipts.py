import sqlite3


def import_receipts():
    conn = sqlite3.connect('../src/files/system_database.sqlite')
    cursor = conn.cursor()
    receipt_process = open('../src/files/receipts.csv', 'r')
    count = 0
    Employee_ID = 0
    Last_Name = 1
    Item = 2
    Units = 3
    Unit_Cost = 4
    Total = 5
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
            cursor.execute("INSERT INTO Receipts VALUES(?,?,?,?,?,?)",(record[Employee_ID], record[Last_Name], record[Item], record[Units], record[Unit_Cost], total_float))
        count += 1
    receipt_process.close()
    conn.commit()
    conn.close()
