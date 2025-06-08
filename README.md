**Support Engineer Coding Challenge**

**Scenario:**

Your team maintains a script that automates the creation of user accounts from a CSV file. A customer reported that new users are not being created correctly. You’ve been assigned to debug and fix the script.

**Challenge Details**

**Problem Statement:**

- The script reads user data from a CSV file (users.csv) and creates users in a mock system by sending HTTP POST requests to an API endpoint.
- The customer provided a sample CSV file and mentioned two issues:
    1. Some user accounts are not created.
    2. The error log is empty even when the script fails.

**Tasks:**

1. **Debug the Script:**  
    Identify and fix the issues in the provided Python script.
2. **Add Features:**
    - Improve error handling so that failed user creations are logged in a file (error_log.txt).
    - Add a feature to skip rows with missing required fields (e.g., email).
3. **Optimize:**
    - Improve the script’s readability and maintainability using best practices (e.g., modular functions, comments).

**Deliverables:**

1. The updated Python script with the issues fixed and features added.
2. A brief explanation (text or comments in the script) of the changes you made.
3. Optional: Suggestions for improving the script further, if any.