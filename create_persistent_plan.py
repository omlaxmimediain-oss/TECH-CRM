import requests
import uuid
import time

BASE_URL = "http://localhost:8000/api"

def test_plan_create_only():
    print("--- Creating Persistent Plan ---")
    
    # 1. Login as Admin
    login_res = requests.post(f"{BASE_URL}/auth/login/", json={
        "phone": "8888888888",
        "password": "admin123"
    })
    if login_res.status_code != 200:
        print(f"Login failed: {login_res.status_code}")
        return
    token = login_res.json()['access']
    headers = {"Authorization": f"Bearer {token}"}
    print("1. Admin logged in.")

    # 2. Get a customer ID
    cust_res = requests.get(f"{BASE_URL}/auth/list/", headers=headers)
    customers = cust_res.json()
    if not customers:
        print("No customers found.")
        return
    cust_id = customers[0]['id']
    
    # 3. CREATE Plan
    plan_payload = {
        "customer_id": cust_id,
        "plan": "R_PRO",
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "status": "ACTIVE"
    }
    create_res = requests.post(f"{BASE_URL}/amc/create/", json=plan_payload, headers=headers)
    print(f"3. CREATE response: {create_res.status_code}")
    if create_res.status_code == 201:
        print(f"SUCCESS: Created Plan for {customers[0]['full_name']}")
    else:
        print(f"FAILED: {create_res.text}")

if __name__ == "__main__":
    test_plan_create_only()
