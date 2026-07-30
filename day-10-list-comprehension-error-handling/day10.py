# Day 10 Mission: List Comprehension & Error Handling

# The Old Way (regular loop)
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)

# The New Way (list comprehension (one liner))
squared = [n ** 2 for n in numbers]
print(squared)


# With the condition — filter and transform at the same time
players_goals = [900, 800, 350, 400, 280]

# Take only those above 500
top_scorers = [g for g in players_goals if g > 500]
print(top_scorers)

# add label at the same time
labeled = [f"{g} goals" for g in players_goals]
print(labeled)


# Without error handling - program will Crash if there's a problem
numbers = int(input("Enter a number: "))    # if user enters a letter, program will Die

# With error handling - program will not crash, but will handle the error gracefully
try:
    numbers = int(input("Enter a number:"))
    print(f"You entered {numbers}")
except ValueError:
    print("That's not a valid number. Please enter a number next time.")

# More detailed example — price input validation
def get_price():
    try:
        price = float(input("Enter the price:"))
        if price < 0:
            print("Price cannot be negative. Please enter a valid price.")
            return None
        return price
    except ValueError:
        print("The input should be a number!")
        return None

result = get_price()
print(result)