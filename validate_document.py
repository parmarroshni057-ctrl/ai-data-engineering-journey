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