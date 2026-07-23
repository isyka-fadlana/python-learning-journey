class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print(f"Your salary {self.__salary}")

    def give_raise(self, amount):
        self.__salary += amount
        if amount < self.__salary:
            print("Raise can't negative")
        elif amount > self.__salary:
            print(f"your salary is raise {self.__salary}")