raw_data = [
    "150",
    "200",
    None,
    "",
    "abc",
    "-50",
    "75",
    "100",
    "NaN",
    "500",
    [],
    {},
    "900",
    "42",
    "-999",
    "hello",
    "1",
    "0",
    "9999",
]

def clean_data(raw_data):
    cleaned_data = []
    for item in raw_data:
        try:
            # Attempt to convert the item to an integer
            number = int(item)
            # Only include non-negative numbers
            if number >= 0:
                cleaned_data.append(number)
        except (ValueError, TypeError):
            # Handle cases where conversion fails or item is not a valid type
            print(f"Invalid data: {item}. Skipping this item.")
    return cleaned_data



def separate_valid_invalid(data):
    valid_data = []
    invalid_data = []
    for item in data:
        try:
            number = int(item)
            if number >= 0:
                valid_data.append(number)
            else:
                invalid_data.append(item)
        except (ValueError, TypeError):
            invalid_data.append(item)
    return valid_data, invalid_data

print("Valid data:", separate_valid_invalid(raw_data)[0])
print("Invalid data:", separate_valid_invalid(raw_data)[1])
