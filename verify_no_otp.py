import os
import django
import sys
import requests

# Setup Django (to check DB directly if needed)
sys.path.append('c:/Users/ADMIN/pro/aanti')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User

def test_registration_no_otp():
    url = "http://localhost:8000/api/auth/register/"
    phone = "8888888888"
    
    # Delete user if exists
    User.objects.filter(phone=phone).delete()
    
    data = {
        "phone": phone,
        "password": "StrongPassword123!",
        "full_name": "Test No OTP",
        "role": "CUSTOMER"
    }
    
    print(f"Attempting registration for {phone} without OTP...")
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 201:
            print("SUCCESS: Registered without OTP!")
        else:
            print("FAILED: Could not register without OTP.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_registration_no_otp()
