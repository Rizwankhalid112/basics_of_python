class BankAccount:
    def __init__(self, amount):
        self.__balance = amount 

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

obj= BankAccount(100)
obj.deposit(200)
print(obj.balance)