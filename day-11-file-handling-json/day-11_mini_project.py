import json
import pandas as pd

contact_data = {
    "name": ["John Doe", "Erick Smith", "Alice Johnson"],
    "phone": ["123-456-7890", "987-654-3210", "555-555-5555"],
    "email": ["john.doe@example.com", "erick.smith@example.com", "alice.johnson@example.com"],
}

# Save the contact data to a JSON file
with open("contact_data.json", "w") as json_file:
    json.dump(contact_data, json_file)

def add_contact(name, phone, email):
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
    }


    try:
        with open("contact_data.json", "r") as json_file:
            contact_data = json.load(json_file)
        with open("contact_data.json", "w") as json_file:
            for key, value in new_contact.items():
                contact_data[key].append(value)
            json.dump(contact_data, json_file)
    except:
        contact_data = {
            "name": [],
            "phone": [],
            "email": [],
        }

        for key, value in new_contact.items():
            contact_data[key].append(value)

        with open("contact_data.json", "w") as json_file:
            json.dump(contact_data, json_file)
        return "New contact added successfully."


def show_contacts():
    try:
        with open("contact_data.json", "r") as json_file:
            contact_data = json.load(json_file)
            df = pd.DataFrame(contact_data)
            return df

    except FileNotFoundError:
        contact_data = {
            "name": [],
            "phone": [],
            "email": [],
        }
        return pd.DataFrame(contact_data)



print(add_contact("Jane Smith", "111-222-3333", "jane.smith@example.com"))
print(show_contacts())
