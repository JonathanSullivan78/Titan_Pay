import sqlite3


def import_timecards():
    conn = sqlite3.connect('../src/files/system_database.sqlite')
    cursor = conn.cursor()
    time_card_processor = open('../src/files/timecards.csv', 'r')
    count = 0
    Employee_ID = 0
    Clock_In = 1
    Clock_Out = 2
    Date = 3
    for line in time_card_processor:
        if count != 0:
            record = line.split(',')
            record[Date] = record[Date].strip()
            cursor.execute("INSERT INTO Time_Cards VALUES(?,?,?,?)", (record[Employee_ID], record[Clock_In], record[Clock_Out], record[Date]))
        count += 1
    time_card_processor.close()
    conn.commit()
    conn.close()
