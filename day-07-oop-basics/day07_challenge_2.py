class BankAccount:
    def __init__(self,owner_name, balance):
        self.owner_name = owner_name
        self.balance    = balance

    def show_account(self):
        print(f"owner name = {self.owner_name}")
        print(f"balance = {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} usd telah masuk ke dalam rekening anda")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"withdraw {amount} usd still in process... ")
            print("Saldo tidak cukup!")

        else:
            self.balance -= amount
            print(f"withdraw {amount} usd still in process... ")
            print("Selamat!! Saldo anda cukup!")

    def check_balance(self):
        print(f"{self.balance} usd")


Miwaastore = BankAccount ("miwaastore", 1000)
erindastore = BankAccount ("erindastore", 2000) 

Miwaastore.show_account()
Miwaastore.deposit(2000)
Miwaastore.withdraw(1200)
Miwaastore.check_balance()