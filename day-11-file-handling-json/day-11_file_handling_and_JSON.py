# Write to a file (creates a new file if it doesn't exist, or overwrites the existing file)
with open ("Notes.txt", "w") as file:
    file.write("This is my first note.\n")
    file.write("Learn file handling in Day 11.\n")

# Read the content of the file and print it
with open ("Notes.txt", "r") as file:
    content = file.read()
    print(content)

# Mode "a" = append, adds content to the end of the file without deleting the previous content.
with open ("Notes.txt", "a") as file:
    file.write("This is an additional note without deleting the previous content.\n")

# Mode "r" = read, reads the content of the file. (line by line)
with open ("Notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())


import json

# Regular Python dictionary
player_data = {
    "name": "John Doe",
    "age": 30,
    "team": "Warriors",
    "goals": 15
}

# Save the dictionary to a JSON file
with open("player_data.json", "w") as json_file:
    json.dump(player_data, json_file)

# Read the JSON file and load it back into a Python dictionary
with open("player_data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    
    print("Player Name:", loaded_data["name"])
    print("Player Age:", loaded_data["age"])
    print("Player Team:", loaded_data["team"])
    print("Player Goals:", loaded_data["goals"])