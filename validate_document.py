documents = [
    {"file_name": "invoice.pdf", "status": "processed"},
    {"file_name": "report.pdf", "status": "pending"},
    {"file_name": "contract.pdf"},
    {"file_name": "receipt.pdf", "status": "processed"},
    {"status": "failed"}
]

valid_documents = []
rejected_documents = []

for document in documents:
    try:
        file_name = document["file_name"]
        status = document["status"]

        valid_documents.append(document)

    except KeyError as error:
        print("Missing field:", error)
        rejected_documents.append(document)
        continue

print("Valid documents:", len(valid_documents))
print("Rejected documents:", len(rejected_documents))

import json

with open("valid_documents.json", "w", encoding="utf-8") as file:
    json.dump(valid_documents, file, indent=4)

with open("rejected_documents.json", "w", encoding="utf-8") as file:
    json.dump(rejected_documents, file, indent=4)

print("Validation results saved successfully")