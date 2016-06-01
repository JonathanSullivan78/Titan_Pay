class BankAccount:
    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = " "
        self.__routing_number = 0
        self.__account_id = 0

    def deposit(self, amt):
        print('Depositing $', amt, ' in ', self.__bank_name , " using Routing Number: " , self.__routing_number)