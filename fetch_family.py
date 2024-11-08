import csv
import requests
from bs4 import BeautifulSoup

# Read credentials from a CSV file
credentials = []
with open("credentials.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        credentials.append({"username": row["username"], "password": row["password"]})

# URL endpoints
login_url = "https://indianvalley.chilipac.com/eg/opac/login?redirect_to=/eg/opac/myopac/main"
circs_url = "https://indianvalley.chilipac.com/eg/opac/myopac/circs"

for credential in credentials:
    # Step 1: Login and capture session cookie
    session = requests.Session()
    payload = {
        "username": credential["username"],
        "password": credential["password"],
        "client_tz": ""  # Adjust time zone if necessary
    }
    login_response = session.post(login_url, data=payload)

    # Check if login was successful and "spark_new_session" cookie exists
    if "spark_new_session" in session.cookies:
        # Step 2: Navigate to circs page
        circs_response = session.get(circs_url)
        
        # Parse the page content
        soup = BeautifulSoup(circs_response.text, 'html.parser')
        checked_items_table = soup.select_one("#myopac_checked_div #acct_checked_main_header tbody")

        if checked_items_table:
            for row in checked_items_table.find_all("tr"):
                title = row.select_one("td:nth-child(3) a").text.strip()
                due_date_text = row.select_one("td:nth-child(6)").text.strip()
                
                # Extract only the date part after "Due Date"
                due_date = due_date_text.replace("Due Date", "").strip()
                
                print(f"Title: {title}, Due Date: {due_date}")
    else:
        print(f"Login failed for username: {credential['username']}")

print("Process complete.")
