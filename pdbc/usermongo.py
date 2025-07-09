import requests
from pymongo import MongoClient, errors

try:
    # Step 1: Fetch data from API
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()  # Raise error for bad response codes
    users = response.json()      # users is already a list of dicts

    # Step 2: Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client['dbtwo']
    collection = db['users']

    # Step 3: Insert data into MongoDB
    collection.insert_many(users)
    print("Data inserted successfully!")

except requests.exceptions.RequestException as e:
    print("API Request Error:", e)

except errors.PyMongoError as e:
    print("MongoDB Error:", e)

except Exception as e:
    print("General Error:", e)

finally:
    try:
        client.close()
    except:
        pass  # In case connection never opened
