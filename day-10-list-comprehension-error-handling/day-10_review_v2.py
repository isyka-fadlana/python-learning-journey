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

def process_data(raw_data):
    valid_data = []
    invalid_data = []
    negative_data = []
    for item in raw_data:
        try:
            number = int(item)
            if number >= 0:
                valid_data.append(number)
            else:
                negative_data.append(number)
        except (ValueError, TypeError):
            invalid_data.append(item)
    return valid_data, invalid_data, negative_data

valid_data, invalid_data, negative_data = process_data(raw_data)
print("Valid data:", valid_data)
print("Invalid data:", invalid_data)
print("Negative data:", negative_data)

total_data = len(raw_data)
print("Total data:", total_data)

valid_count = len(valid_data)
invalid_count = len(invalid_data)
negative_count = len(negative_data)
print("Count of valid data:", valid_count)
print("Count of invalid data:", invalid_count)
print("Count of negative data:", negative_count)

print("Summary:")
print("------")
print(total_data)

def calculate_percentage(count, total):
    if total == 0:
        return 0
    return (count / total) * 100

valid_percentage = calculate_percentage(valid_count, total_data)
invalid_percentage = calculate_percentage(invalid_count, total_data)
negative_percentage = calculate_percentage(negative_count, total_data)

print("Percentage of valid data:", valid_percentage)
print("Percentage of invalid data:", invalid_percentage)
print("Percentage of negative data:", negative_percentage)