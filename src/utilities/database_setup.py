import sqlite3


def create_database():
    con = sqlite3.connect('../files/system_database.sqlite')
    c = con.cursor()
    # Hourly Employee Table
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn='Hourly_Employees', nf='Employee_ID', ft='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Hourly_Employees', cn='Last_Name', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Hourly_Employees', cn='First_Name', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Hourly_Employees', cn='Hourly_Rate', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Hourly_Employees', cn='Union_Dues', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Hourly_Employees', cn='Payment_Method', ct='TEXT'))
    # Salaried Employee Table
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn='Salaried_Employees', nf='Employee_ID', ft='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='Last_Name', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='First_Name', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='Salary_Rate', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='Commission_Rate', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='Union_Dues', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Salaried_Employees', cn='Payment_Method', ct='TEXT'))
    # Time Card Table
    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn='Time_Cards', nf='Employee_ID', ft='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Time_Cards', cn='Clock_In', ct='INTEGER'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Time_Cards', cn='Clock_Out', ct='INTEGER'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Time_Cards', cn='Date', ct='TEXT'))
    # Receipt Table
    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn='Receipts', nf='Employee_ID', ft='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Receipts', cn='Last_Name', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Receipts', cn='Item', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Receipts', cn='Units', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Receipts', cn='Unit_Cost', ct='TEXT'))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn='Receipts', cn='Total', ct='TEXT'))
    # Finalize
    con.commit()
    con.close()

create_database()