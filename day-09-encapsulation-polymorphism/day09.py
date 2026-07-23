class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance  = balance               # ⬅️ underscore ganda = "private"

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit berhasil. Saldo: {self.__balance}")
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Isyka", 1000)
print(account.deposit(3000))
print(account.get_balance())
