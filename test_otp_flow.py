
import requests
import uuid

BASE_URL = "http://localhost:8000/api"

def register_user(phone, otp=None, password="Str0ngPassword!123"):
    unique_name = f"OTP User {uuid.uuid4().hex[:8]}"
    payload = {
        "phone": phone,
        "password": password,
        "full_name": unique_name,
        "role": "CUSTOMER",
        "otp": otp
    }
    try:
        response = requests.post(f"{BASE_URL}/auth/register/", json=payload)
        return response
    except Exception as e:
        print(f"Register Request failed: {e}")
        class MockResponse:
            status_code = 500
            text = str(e)
        return MockResponse()

def send_otp(phone):
    try:
        response = requests.post(f"{BASE_URL}/auth/send-otp/", json={"phone": phone})
        return response
    except Exception as e:
        print(f"Send OTP Request failed: {e}")
        return None

def test_otp_flow():
    print("--- Starting OTP Flow Tests ---")

    phone = f"91{str(uuid.uuid4().int)[:8]}" # Random 10 digit
    
    # 1. Register without OTP (Should Fail)
    print("\n1. Testing Register without OTP...")
    res = register_user(phone)
    if res.status_code == 400 and "request an OTP first" in res.text:
         print(f"[PASS] Missing OTP rejected correctly.")
    else:
         print(f"[FAIL] Missing OTP result: {res.status_code} - {res.text}")

    # 2. Send OTP
    print("\n2. Sending OTP...")
    otp_res = send_otp(phone)
    if otp_res.status_code == 200:
        data = otp_res.json()
        otp_code = data.get('debug_otp')
        print(f"[PASS] OTP Sent. Debug Code: {otp_code}")
    else:
        print(f"[FAIL] Send OTP failed: {otp_res.status_code} - {otp_res.text}")
        return

    # 3. Register with Wrong OTP (Should Fail)
    print("\n3. Testing Register with Wrong OTP...")
    res = register_user(phone, otp="000000")
    if res.status_code == 400 and "Invalid OTP" in res.text:
         print(f"[PASS] Wrong OTP rejected correctly.")
    else:
         print(f"[FAIL] Wrong OTP result: {res.status_code} - {res.text}")

    # 4. Register with Correct OTP (Should Pass)
    print("\n4. Testing Register with Correct OTP...")
    res = register_user(phone, otp=otp_code)
    if res.status_code == 201:
         print(f"[PASS] Correct OTP accepted. User created.")
    else:
         print(f"[FAIL] Correct OTP result: {res.status_code} - {res.text}")

    print("\n--- Tests Completed ---")

if __name__ == "__main__":
    test_otp_flow()
