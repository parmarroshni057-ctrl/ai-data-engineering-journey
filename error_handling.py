import json

try:
    with open("invalid.json", "r", encoding="utf-8") as file:
        documents = json.load(file)

    print("File loaded successfully")
    print("Total documents:", len(documents))

except FileNotFoundError:
    print("Error: File does not exist")

except json.JSONDecodeError:
    print("Error: Invalid JSON format")