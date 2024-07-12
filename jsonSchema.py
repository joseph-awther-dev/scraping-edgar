# import requests
# from pymongo import MongoClient
# import base64
# import json
# from datetime import datetime

# # GitHub repository information
# github_user = "dev2@awther.com"
# github_pass = "@ABcd123@ABcd123"
# repo_owner = "awtherllc"
# repo_name = "XsdToJsonSchema"
# repo_branch = "main"

# # MongoDB connection information
# mongo_client = MongoClient("mongodb://root:demo1234@127.0.0.1:27017/")
# db = mongo_client["root"]
# collection = db["demo1234"]

# # Get list of files in the repository
# repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/{repo_branch}?recursive=1"
# response = requests.get(repo_url, auth=(github_user, github_pass))

# print(response)
# # if response.status_code == 200:
# #     file_list = response.json().get("tree", [])
# #     json_files = [file for file in file_list if file["path"].endswith(".json")]
    
# #     for file in json_files:
# #         file_url = file["url"]
# #         file_response = requests.get(file_url, auth=(github_user, github_pass))
        
# #         if file_response.status_code == 200:
# #             file_content = file_response.json().get("content")
# #             file_data = json.loads(base64.b64decode(file_content).decode('utf-8'))
            
# #             # Determine the type of JSON file
# #             if "UIschema" in file_data:
# #                 file_type = "UIschema"
# #             elif "Rules" in file_data:
# #                 file_type = "Rules"
# #             else:
# #                 file_type = "schema"

# #             # Prepare document for MongoDB
# #             document = {
# #                 "file_name": file["path"],
# #                 "file_type": file_type,
# #                 "file_data": file_data,
# #                 "created_at": datetime.utcnow()  # Add the created_at field
# #             }
            
# #             # Insert document into MongoDB
# #             collection.insert_one(document)
# #             print(f"Inserted {file['path']} as {file_type} into MongoDB")
# #         else:
# #             print(f"Failed to retrieve {file['path']}")
# # else:
# #     print("Failed to get the file list from the repository")


import os
import json
from pymongo import MongoClient
from datetime import datetime

# Local folder containing JSON files
# folder_path = "C:\Users\JosephSantiago\Documents\project\awther_api\reactSecClient\src\components\edgarSubmission\schema\json"
folder_path = r"C:\Users\JosephSantiago\Documents\project\awther_api\reactSecClient\src\components\edgarSubmission\schema\json"

# MongoDB connection information
mongo_client = MongoClient("mongodb://root:demo1234@127.0.0.1:27017/")
db = mongo_client["root"]
collection = db["demo1234"]

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, "r") as file:
            file_data = json.load(file)
            
            # Determine the type of JSON file
            if "UIschema" in file_name:
                file_type = "UI"
            elif "Rules" in file_name:
                file_type = "Rules"
            else:
                file_type = "schema"
            
            # Prepare document for MongoDB
            document = {
                "file_name": file_name,
                "file_type": file_type,
                "file_data": file_data,
                "created_at": datetime.utcnow()  # Add the created_at field
            }
            
            # Insert document into MongoDB
            collection.insert_one(document)
            print(f"Inserted {file_name} as {file_type} into MongoDB")
