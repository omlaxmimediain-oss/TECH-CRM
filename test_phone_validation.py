
import requests
import uuid

BASE_URL = "http://localhost:8000/api"

def register_user(phone, password="Str0ngPassword!123"):
    unique_name = f"Test User {uuid.uuid4().hex[:8]}"
    payload = {
        "phone": phone,
        "password": password,
        "full_name": unique_name,
        "role": "CUSTOMER"
    }
    try:
        response = requests.post(f"{BASE_URL}/auth/register/", json=payload)
        return response
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def test_phone_validation():
    print("--- Starting Phone Validation Tests ---")

    # 1. Valid Phone (10 digits)
    phone_valid = f"90{uuid.uuid4().int}"[:10] # Generate random 10 digit
    res = register_user(phone_valid)
    if res.status_code == 201:
        print(f"[PASS] Valid phone {phone_valid} registered successfully.")
    else:
        print(f"[FAIL] Valid phone {phone_valid} failed: {res.text}")

    # 2. Invalid Length (< 10)
    phone_short = "123456789"
    res = register_user(phone_short)
    if res.status_code == 400 and "exactly 10 digits" in res.text:
         print(f"[PASS] Short phone {phone_short} rejected correctly.")
    else:
         print(f"[FAIL] Short phone {phone_short} result: {res.status_code} - {res.text}")

    # 3. Invalid Length (> 10)
    phone_long = "12345678901"
    res = register_user(phone_long)
    if res.status_code == 400 and "exactly 10 digits" in res.text:
         print(f"[PASS] Long phone {phone_long} rejected correctly.")
    else:
         print(f"[FAIL] Long phone {phone_long} result: {res.status_code} - {res.text}")

    # 4. Duplicate Check
    res_dup = register_user(phone_valid)
    if res_dup.status_code == 400 and "already registered" in res_dup.text:
         print(f"[PASS] Duplicate phone {phone_valid} rejected correctly.")
    else:
         print(f"[FAIL] Duplicate phone {phone_valid} result: {res_dup.status_code} - {res_dup.text}")

    print("--- Tests Completed ---")

if __name__ == "__main__":
    test_phone_validation()
