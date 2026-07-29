class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print(f"Your salary {self.__salary}")

    def give_raise(self, amount):
        if amount < 0:
            print("Raise can't be negative")
        else:
            self.__salary += amount
            print(f"Your salary is raised to {self.__salary}")

employee = Employee(5000)
employee.get_salary()
employee.give_raise(500)
employee.get_salary()

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes =[Square(1), Circle(1)]

for shape in shapes:
        print(shape.area())
