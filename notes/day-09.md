# Day 9 — Encapsulation & Polymorphism

## Goal
Understand the final two pillars of Object-Oriented Programming (OOP): Encapsulation (protecting data) and Polymorphism (one method, many different behaviours).

## What I Learned
- Use private attributes with `__` (double underscore) to prevent direct access or modification from outside the class.
- Access private data through dedicated methods such as `get_salary()` and `give_raise()`.
- Create a parent class with a base method, then override that method in child classes with different implementations.
- Understand polymorphism by storing different objects in the same list and calling the same method (`area()`), where each object produces a different result based on its own class.

## Mistakes
1. The logic inside `give_raise()` was in the wrong order—I increased the salary before validating the input (similar to the `withdraw()` bug from Day 7).
2. I created the class but forgot to instantiate an object and call its methods, so the program produced no output.
3. Indentation error—the line `for shape in shapes:` was indented when it should have been aligned to the left, causing Python to misinterpret the code structure.
4. Variable naming typo—I declared `shape` (singular) but used `shapes` (plural) inside the loop.

## How I Fixed It
- Always **validate first, then perform the action**. For example, check `if amount < 0` before modifying the salary.
- Remember that a class is only a blueprint. You must create an object (instantiate it) and call its methods for the program to do anything.
- When facing an indentation error, carefully compare each line and make sure the indentation level matches the intended code structure.
- Keep variable names consistent from declaration to usage throughout the code.

## Insights
A class is like a robot—it doesn't just store data, it also has behaviour. The private attribute `__salary` protected by encapsulation is like a bank vault. Customers cannot access the money directly; they must go through a bank teller, who first validates whether the transaction is allowed. Encapsulation is not only about hiding data—it is about protecting the integrity of the data by preventing invalid operations, such as making a salary negative or changing it into a string.

## Projects / Challenges
- **BankAccount** with balance validation (Day 7 concept review)
- **Employee** with a private `__salary` attribute and a validated `give_raise()` method
- **Shape → Square & Circle** demonstrating polymorphism through the `area()` method