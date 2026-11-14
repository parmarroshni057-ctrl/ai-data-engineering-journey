documents = [
    {"file_name": "invoice.pdf", "status": "processed"},
    {"file_name": "report.pdf", "status": "pending"},
    {"file_name": "contract.pdf"},
    {"file_name": "receipt.pdf", "status": "processed"},
    {"status": "failed"}
]

for document in documents:
    try:
        #if "file_name" in document and "status" in document:
                print("Processing: ",document["file_name"], document["status"])
    except KeyError as error: #error is a variable holding the exception object.
        print("Missing:" , error)   
        continue  # Skip to the next document if a required field is missing, if continue is not used, the program will terminate and not process the remaining documents.

    
              