# Day 10 — List Comprehension & Error Handling

## Goal
Understand how to write more concise code using list comprehensions and how to handle errors gracefully so that programs don't crash unexpectedly.

## What I Learned
- **List comprehension:** `[expression for item in list]` — a concise way to create a new list from an existing one, with optional filtering using `if`.
- **try/except:** Catch specific exceptions (such as `ValueError`) so the program can continue running even when invalid input is encountered.
- The placement of a `try` block determines how much of the process is affected when an error occurs.

## Mistakes
I placed the `try/except` block **outside** the list processing (wrapping the entire operation) instead of handling errors **inside** the loop for each individual item. As a result, a single invalid value (such as `"abc"`) caused the entire conversion process to fail, rather than skipping only the invalid entry while continuing with the remaining valid data.

## How I Fixed It
Move the `try/except` block **inside** the loop so that each item is processed independently. This way, if one item raises an exception, it is skipped while the loop continues processing the rest of the data.

## Insights
This introduces the concept of **Fail Fast vs. Graceful Degradation**:

- **Fail Fast:** A single `try` block wraps the entire process, so one error causes the whole operation to fail. It's like putting all your clothes in one washing machine—if a rock gets inside, the entire wash cycle is affected.
- **Graceful Degradation:** Each iteration has its own `try` block, so one error only affects the current item while the rest continue processing. It's like washing clothes one at a time—if you find a rock, you remove it and continue washing the remaining clothes.

In real-world applications, such as cleaning client data, **Graceful Degradation** is usually the better approach. Clients would rather have **995 out of 1,000 records processed successfully** than have the entire process fail because of just **5 invalid records**.

## Project / Challenge
**Data Cleaner** — Build a `clean_data(raw_list)` function that accepts a list of messy data (a mix of valid numbers, text, and empty strings) and returns a cleaned list containing only valid numbers, while continuing to process the remaining data even if invalid values are encountered.