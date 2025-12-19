
from pymongo import MongoClient

# MongoDB Connection Setup
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['mydatabase']  # Replace with your database name
collection = db['mycollection']  # Replace with your collection name

# Query to Find Documents
query = {"status": "active"}  # Example query to find active records
result = collection.find(query)

# Validation Function
def validate_output(doc):
    # Example validation: Check if "status" is "active" and "age" is > 18
    return doc.get("status") == "active" and doc.get("age", 0) > 18

# Process and Validate Results
for document in result:
    print("Document:", document)
    if validate_output(document):
        print("✅ Validation Passed")
    else:
        print("❌ Validation Failed")

# Close the Connection
client.close()
