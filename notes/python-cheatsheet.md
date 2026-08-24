# List Comprehension

## Purpose

Create a new list using a more concise syntax.

## Syntax

[expression for item in iterable]

## With condition

[expression for item in iterable if condition]

## Good for

- Simple transformations
- Simple filtering
- Creating new lists

## Avoid when

- The logic is too complex
- There are many nested loops
- Readability decreases

# Exception Handling

## Purpose

Handle errors that occur while the program is running.

## Basic structure

try:
    risky_operation()

except ValueError:
    handle_error()

## Flow

try
↓
operation
↓
success → continue

OR

error
↓
except
↓
handle/recover

## Important exceptions

ValueError
→ The value is not appropriate for the operation

TypeError
→ The data type is not appropriate

# Defensive Programming

Thinking about possible abnormal conditions
before the program runs.

Example:

if total == 0:
    return 0

# DRY

Don't Repeat Yourself.

If the same logic is used multiple times,
consider creating a reusable function.

# Important Engineering Principle

Data validity is determined based on:

1. Can the data be processed?
2. Does the data meet the business rules?

Example:

"150"
→ conversion succeeds
→ valid

"-50"
→ conversion succeeds
→ business rule fails
→ negative

"abc"
→ conversion fails
→ invalid