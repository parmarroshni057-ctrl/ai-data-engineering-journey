import json

with open("document.json", "r", encoding="utf-8") as file:
    documents = json.load(file)

print(documents)  # Output: [{'file_name': 'invoice.pdf', 'status': 'processed'}, {'file_name': 'report.pdf', 'status': 'pending'}, {'file_name': 'contract.pdf', 'status': 'failed'}, {'file_name': 'receipt.pdf', 'status': 'processed'}, {'file_name': 'application.pdf', 'status': 'failed'}]

for document in documents:
    print(document["file_name"])  # Output: invoice.pdf, report.pdf, contract.pdf
    print(type(document))  # Output: <class 'dict'>

print(type(documents))  # Output: <class 'list'>