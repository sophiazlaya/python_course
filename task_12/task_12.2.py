class BankAccount:
    def __init__(self, customers_name, account_number, balance, password):
        self.customers_name = customers_name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            print('your balance is', self.__balance, 'dollars')

    def change_balance(self, password, new_balance):
        if password == self.__password:
            self.__balance = new_balance + self.__balance


Nick = BankAccount('Nick', 547, 150, 'qwerty')
Nick.change_balance(input('if you want to change the balance enter the password'), int(input('deposit money')))
Nick.get_balance(input('if you want to know the balance enter the password'))