import csv
import requests
import logging

# Configure logging
logging.basicConfig(
    filename='error_log.txt', # Log to a file named 'error_log.txt'
    level=logging.INFO, # Set to INFO to capture all messages of severity INFO and above
    format='%(asctime)s - %(levelname)s - %(message)s' 
)

def create_users(file_path,api_url):
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            # Check if CSV file has expected headers
            if not reader.fieldnames:
                logging.error(f"CSV file '{file_path}' is empty or has no headers.")
                print(f"Error: CSV file '{file_path}' is empty or has no headers. Check error_log.txt for details.")
                return

            for row_num, row in enumerate(reader, start=2): # Start counting from 2 for row numbers (header is row 1)
                # Basic validation for empty values
                if all(value and value.strip() != '' for value in row.values()):
                    try:
                        response = requests.post(api_url, json=row, timeout=10) # Added timeout
                        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)

                        print(f"Successfully created user: {row.get('name', 'N/A')}")

                    except requests.exceptions.RequestException as e:
                        user_name = row.get('name', 'N/A')
                        error_message = f"API request failed for user '{user_name}' (row {row_num}): {e}"
                        logging.error(error_message)
                        print(f"Error creating user: {user_name}. Check error_log.txt for details.")
                    except Exception as e:
                        user_name = row.get('name', 'N/A')
                        error_message = f"An unexpected error occurred for user '{user_name}' (row {row_num}): {e}"
                        logging.error(error_message)
                        print(f"An unexpected error occurred for user: {user_name}. Check error_log.txt for details.")
                else:
                    user_name = row.get('name', 'N/A')
                    logging.warning(f"Skipped user (row {row_num}): '{user_name}' - Missing required fields.")
                    print(f"Skipped creating user: {user_name} - Missing required fields.")
    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at '{file_path}'.")
        print(f"Error: CSV file not found at '{file_path}'. Please ensure the file exists.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while processing the file: {e}")
        print(f"An unexpected error occurred while processing the file. Check error_log.txt for details.")

# Example usage:
create_users("users.csv", "https://example.com/api/create_user")
# Note: Replace "https://example.com/api/create_user" with the actual API endpoint URL.
# Ensure the CSV file 'users.csv' exists in the same directory or provide the correct path.