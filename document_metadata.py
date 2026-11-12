document = {
    "file_name": "invoice.pdf",
    "pages": 5,
    "status": "pending"
}

print(document["file_name"])  # Output: invoice.pdf

document["status"] = "processed"  # Update status
document["document_type"] = "invoice"  # Add new key-value pair

print(document)  # Output: {'file_name': 'invoice.pdf', 'pages': 5, 'status': 'processed', 'document_type': 'invoice'}
print(len(document))  # Output: 4


