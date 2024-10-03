import os
import csv
import pymongo

# Function to parse CSV and store data in MongoDB
def parse_and_store_csv(file_path):
    try:
        # Open the file safely, ensuring it's accessible
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Connect to MongoDB
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["medalist_db"]
            collection = db["medalists"]

            # Insert each row into MongoDB
            for row in csv_reader:
                # Insert only if it doesn't exist (avoiding duplicates)
                collection.update_one(
                    {'name': row['name'], 'medal_date': row['medal_date']},
                    {'$set': row},
                    upsert=True
                )
        print(f"File processed successfully: {file_path}")
    
    except PermissionError as pe:
        print(f"Permission error: {pe}")
    except Exception as e:
        print(f"An error occurred: {e}")

