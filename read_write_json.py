import json

with open("document.json", "r", encoding="utf-8") as file:
    documents = json.load(file)

def show_document_status(status):
    if status == "processed":
        return "Processing complete"
    elif status == "pending":
        return "Waiting for processing"
    return "Investigate document"

for document in documents:
    document["message"] = show_document_status(document["status"])  # Add message key-value pair

with open("processed_documents.json", "w", encoding="utf-8") as file:
    json.dump(documents, file, indent=4)