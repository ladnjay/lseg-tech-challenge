Support Engineer Coding Challenge

Scenario:
Your team maintains a script that automates the creation of user accounts from a CSV file. A customer reported that new users are not being created correctly. You’ve been assigned to debug and fix the script.

Challenge Details

Problem Statement:
The script reads user data from a CSV file (users.csv) and creates users in a mock system by sending HTTP POST requests to an API endpoint.

The customer provided a sample CSV file and mentioned two issues: 
Some user accounts are not created.
The error log is empty even when the script fails.

Tasks:
Debug the Script:
Identify and fix the issues in the provided Python script.

Add Features:
Improve error handling so that failed user creations are logged in a file (error_log.txt).

Add a feature to skip rows with missing required fields (e.g., email).

Optimize:
Improve the script’s readability and maintainability using best practices (e.g., modular functions, comments).

Deliverables:
The updated Python script with the issues fixed and features added.
A brief explanation (text or comments in the script) of the changes you made.

Optional: 
Suggestions for improving the script further, if any.


Evaluation Criteria:
Debugging: Ability to identify and resolve errors in the script.

Coding Skills: 
Writing clean, efficient, and maintainable code.

Error Handling: 
Properly logging errors and managing edge cases.

Problem-Solving: 
Addressing the requirements and suggesting improvements.

Sample users.csv 

name,email,role
Alice,alice@example.com,admin
Bob,,user
Charlie,charlie@example.com,moderator

Initial python script

import csv
import requests

def create_users(file_path):
        with open(file_path, 'r') as f:
                 reader = csv.DictReader(f)
                 for row in reader:
                       response = requests.post("https://example.com/api/create_user", json=row)
                       if response.status_code != 201:
                              print("Error creating user:", row["email"])

create_users("users.csv")