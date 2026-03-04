class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    # 1. The Getter
    @property
    def balance(self):
        print("Checking balance...")
        return self.__balance

 
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: You cannot have a negative balance!")
        else:
            print(f"Updating balance to {value}")
            self.__balance = value
    @balance.deleter
    def balance(self):
        print("Warning: Deleting the balance attribute!")
        del self.__balance


acc = BankAccount(100)

print(acc.balance) 

acc.balance = 200  
acc.balance = -50 e
print(acc.balance)
print(acc.balance)