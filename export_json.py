import json

document = {
    "file_name": "invoice.pdf",
    "status": "processed"
}

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(document, file, indent=4)