import requests
import uuid
import time

BASE_URL = "http://localhost:8000/api"

def test_plan_crud():
    print("--- Starting Plan CRUD Verification ---")
    
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
        print("No customers found. Please create one.")
        return
    cust_id = customers[0]['id']
    print(f"2. Using customer: {customers[0]['full_name']} ({cust_id})")

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
    if create_res.status_code != 201:
        print(f"FAILED CREATE: {create_res.text}")
        return
    sub = create_res.json()
    sub_id = sub['id']
    print(f"3. Created Plan ID: {sub_id}, Plan: {sub['plan']}, Amount: {sub['subscription_amount']}")

    # 4. UPDATE Plan (Change plan type)
    update_payload = {
        "plan": "R_ELITE",
        "status": "ACTIVE"
    }
    update_res = requests.patch(f"{BASE_URL}/amc/{sub_id}/admin/", json=update_payload, headers=headers)
    print(f"4. UPDATE response: {update_res.status_code}")
    if update_res.status_code != 200:
        print(f"FAILED UPDATE: {update_res.text}")
    else:
        updated_sub = update_res.json()
        print(f"4. Updated Plan: {updated_sub['plan']}, Amount: {updated_sub['subscription_amount']} (Should be 8000.00)")

    # 5. DELETE Plan
    del_res = requests.delete(f"{BASE_URL}/amc/{sub_id}/admin/", headers=headers)
    print(f"5. DELETE response: {del_res.status_code}")
    if del_res.status_code == 204:
        print("--- SUCCESS: Plan CRUD Verification Completed ---")
    else:
        print(f"--- FAILED DELETE: {del_res.text} ---")

if __name__ == "__main__":
    test_plan_crud()
