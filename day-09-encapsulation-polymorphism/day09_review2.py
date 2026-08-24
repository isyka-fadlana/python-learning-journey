class BankAccount:
    def __init__(self, owner_name, balance):

        if not isinstance(owner_name, str):
            raise ValueError("Owner name must be a string")

        if not isinstance(owner_name.strip(), str):
            raise ValueError("Owner name cannot be empty")

        if isinstance(balance, bool) or not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number")
        
        if balance < 0:
            raise ValueError("Balance must be a non-negative number")
        
        self.__owner_name = owner_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Deposit amount must be a number")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance


    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Withdrawal amount must be a number")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
        return self.__balance

account = BankAccount("John Doe", 500)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())