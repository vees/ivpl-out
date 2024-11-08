# Library Account Automation Script

This Python script automates login and data retrieval from the Indian Valley library's account system. Given a CSV file with usernames and passwords, the script logs into each account, navigates to the user’s circulation page, and extracts titles and due dates of checked-out items.

## Prerequisites

1. Python 3.6 or higher
2. Required libraries:
   - `requests`: for handling HTTP requests
   - `beautifulsoup4`: for parsing HTML

Install these packages using:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Prepare Credentials File**: Create a CSV file named `credentials.csv` in the same directory as the script, with the following structure:

   ```csv
   username,password
   12345,1234
   12346,1235
   12347,1236
   12348,1237
   ```

2. **Run the Script**: Execute the script with:

   ```bash
   python3 fetch_family.py
   ```

3. **Output**: For each username, the script will print the titles and due dates of all checked-out items.

## Script Overview

1. **Login**: The script reads usernames and passwords from `credentials.csv` and attempts to log in to each account.
2. **Data Extraction**: After a successful login, it navigates to the circulation page and scrapes the book titles and due dates.
3. **Result**: Outputs titles and due dates in the console.

## Notes

- Ensure `credentials.csv` is formatted correctly, with `username` and `password` columns.
- This script is designed specifically for the Indian Valley library's system structure. Adjustments may be needed for other systems.

