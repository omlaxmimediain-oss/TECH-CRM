import requests
import json

base_url = "http://localhost:8000/api"

# Login as customer
login_data = {
    "phone": "1234567890",  # Updated phone
    "password": "password123"
}

login_res = requests.post(f"{base_url}/auth/login/", json=login_data)
if login_res.status_code != 200:
    print(f"Login failed: {login_res.text}")
    exit()

token = login_res.json()["access"]
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# Try to create ticket
ticket_data = {
    "issue_description": "Internet is slow",
    "location_address": "123 Main St",
    "location_latitude": 28.6139,
    "location_longitude": 77.2090,
    "job_value": 500,
    "is_emergency": False
}

ticket_res = requests.post(f"{base_url}/tickets/create/", json=ticket_data, headers=headers)
print(f"Status Code: {ticket_res.status_code}")
print(f"Response: {ticket_res.text}")
