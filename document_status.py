document = {
    "file_name": "invoice.pdf",
    "status": "processed",
    "pages": 5
}

print(document["file_name"])  # Output: invoice.pdf

if document["status"] == "processed":
    print("Processing complete")  # Output: Processing complete
elif document["status"] == "pending":
    print("Waiting for processing")  # Output: Waiting for processing
else:
    print("Investigate document")  # Output: Investigate document


documents = [
    {"file_name": "invoice.pdf", "status": "processed"},
    {"file_name": "report.pdf", "status": "pending"},
    {"file_name": "contract.pdf", "status": "failed"},
    {"file_name": "receipt.pdf", "status": "processed"},
    {"file_name": "application.pdf", "status": "failed"}
]

for document in documents:
    print(document["file_name"])  # Output: invoice.pdf, report.pdf, contract.pdf
    if document["status"] == "processed":
        print("Processing complete")  # Output: Processing complete
    elif document["status"] == "pending":
        print("Waiting for processing")  # Output: Waiting for processing
    else:
        print("Investigate document")  # Output: Investigate document

def show_document_status(status):
    if status == "processed":
        return "Processing complete"
    elif status == "pending":
        return "Waiting for processing"
    else:
        return "Investigate document"

for document in documents:
    #print(document["file_name"])  # Output: invoice.pdf, report.pdf, contract.pdf
    #print(show_document_status(document["status"]))  # Output: Processing complete, Waiting for processing, Investigate document
    document["message"] = show_document_status(document["status"])  # Add message key-value pair

print(documents)  # Output: [{'file_name': 'invoice.pdf', 'status': 'processed', 'message': 'Processing complete'}, {'file_name': 'report.pdf', 'status': 'pending', 'message': 'Waiting for processing'}, {'file_name': 'contract.pdf', 'status': 'failed', 'message': 'Investigate document'}]

processed_count = 0
pending_count = 0
failed_count = 0

for document in documents:
    if document["status"] == "processed":
        processed_count += 1
    elif document["status"] == "pending":
        pending_count += 1
    else:
        failed_count += 1

print(processed_count)  # Output: 2
print(pending_count)  # Output: 1
print(failed_count)  # Output: 2