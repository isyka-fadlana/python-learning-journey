data = ["100", "200", "abc", "300", "", "150", "xyz",]
try: int_data = [int(i) for i in data]
except ValueError:
    print("Data contains non-integer values. Please check the input data.")

list_numbers = [100, 200, 300, 150]
print(f"List of numbers: {list_numbers}")

def clean_data(raw_list):
    received_worst_list = []
    for item in raw_list:
        try:
            received_worst_list.append(int(item))
        except ValueError:
            print(f"Invalid data: {item}. Skipping this item.")

    cleaned_list = [num for num in received_worst_list if num >= 0]
    return cleaned_list

print(f"Cleaned list: {clean_data(data)}")