
import requests
import json

BASE_URL = "http://localhost:8000/api"
ADMIN_PHONE = "9999999999"  
ADMIN_PASS = "admin123" 

def get_tokens(phone, password):
    url = f"{BASE_URL}/auth/login/"
    payload = {"phone": phone, "password": password}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Login failed: {e}")
        if response:
            print(response.text)
        return None

def run_tests():
    print("--- Starting Plan CRUD Tests ---")
    
    # 1. Login
    tokens = get_tokens(ADMIN_PHONE, ADMIN_PASS)
    if not tokens:
        return
    
    headers = {
        "Authorization": f"Bearer {tokens['access']}",
        "Content-Type": "application/json"
    }

    # 2. LIST Plans
    print("\n--- Listing Plans ---")
    res = requests.get(f"{BASE_URL}/amc/plans/", headers=headers)
    if res.status_code == 200:
        plans = res.json()
        print(f"Found {len(plans)} plans.")
        if len(plans) > 0:
            print(f"Sample Plan: {plans[0]['name']} ({plans[0]['code']})")
    else:
        print(f"Failed to list plans: {res.status_code} - {res.text}")
        return

    # 3. CREATE Plan
    print("\n--- Creating New Plan ---")
    new_plan_data = {
        "name": "Test Protocol Omega",
        "code": "T_OMEGA",
        "category": "Industrial",
        "visits": 100,
        "price": 9999.00,
        "color_theme": "red",
        "is_active": True
    }
    res = requests.post(f"{BASE_URL}/amc/plans/", json=new_plan_data, headers=headers)
    if res.status_code == 201:
        created_plan = res.json()
        plan_id = created_plan['id']
        print(f"Plan Created: {created_plan['name']} (ID: {plan_id})")
    else:
        print(f"Failed to create plan: {res.status_code} - {res.text}")
        return

    # 4. UPDATE Plan
    print("\n--- Updating Plan ---")
    update_data = {"name": "Test Protocol Omega (Revised)", "price": 8888.00}
    res = requests.patch(f"{BASE_URL}/amc/plans/{plan_id}/", json=update_data, headers=headers)
    if res.status_code == 200:
        updated_plan = res.json()
        print(f"Plan Updated: {updated_plan['name']} - Price: {updated_plan['price']}")
    else:
        print(f"Failed to update plan: {res.status_code} - {res.text}")

    # 5. CREATE Subscription with New Plan
    print("\n--- Creating Subscription with New Plan ---")
    # Fetch a customer first
    cust_res = requests.get(f"{BASE_URL}/auth/list/", headers=headers)
    customers = cust_res.json()
    if not customers:
        print("No customers found to subscribe.")
    else:
        customer_id = customers[0]['id']
        print(f"Using Customer: {customers[0]['full_name']}")
        
        sub_data = {
            "customer_id": customer_id,
            "plan_id": plan_id,
            "start_date": "2025-01-01",
            "end_date": "2026-01-01",
            "status": "ACTIVE"
        }
        sub_res = requests.post(f"{BASE_URL}/amc/create/", json=sub_data, headers=headers)
        if sub_res.status_code == 201:
            sub = sub_res.json()
            print(f"Subscription Created! ID: {sub['id']}")
            print(f"Plan Attached: {sub['plan_details']['name']}")
            
            # Cleanup Subscription
            requests.delete(f"{BASE_URL}/amc/{sub['id']}/admin/", headers=headers)
            print("Subscription Cleaned up.")
        else:
             print(f"Failed to create subscription: {sub_res.status_code} - {sub_res.text}")


    # 6. DELETE Plan
    print("\n--- Deleting Plan ---")
    res = requests.delete(f"{BASE_URL}/amc/plans/{plan_id}/", headers=headers)
    if res.status_code == 204:
        print("Plan Deleted (Soft Delete Check)")
        # Verify it's gone from list (or inactive)
        check_res = requests.get(f"{BASE_URL}/amc/plans/{plan_id}/", headers=headers)
        if check_res.status_code == 200:
            p = check_res.json()
            print(f"Plan is_active status: {p.get('is_active')}")
    else:
         print(f"Failed to delete plan: {res.status_code} - {res.text}")

    print("\n--- Tests Completed ---")

if __name__ == "__main__":
    run_tests()
