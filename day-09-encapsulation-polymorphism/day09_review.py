# Encapsulation and Polymorphism
class BankAccount:
    def __init__(self, owner_name, balance):

        if not isinstance(owner_name, str):
            raise ValueError("Owner name must be a string")
        
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number")
        
        self.__owner_name = owner_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Your balance is raised to {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount        # balance reduced by the amount withdrawn

account = BankAccount("John Doe", 500)

account.deposit(500)
account.withdraw(200)
print(account.get_balance())

# Continue with the next part of the code
import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)     
            
shapes = [Square(4), Circle(3)]

for shape in shapes:
    print(shape.area())
