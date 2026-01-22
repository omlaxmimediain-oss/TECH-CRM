import os
import django
import json
from rest_framework.test import APIClient
from apps.accounts.models import User

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def debug_endpoints():
    client = APIClient()
    
    # Use the known superadmin phone
    try:
        admin_user = User.objects.get(phone='8888888888')
        client.force_authenticate(user=admin_user)
        print(f"Authenticated as: {admin_user.phone} ({admin_user.role})")
    except User.DoesNotExist:
        print("Admin user 8888888888 not found!")
        return

    # Debug Customers List
    print("\n--- Debugging /api/auth/list/ ---")
    response = client.get('/api/auth/list/')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Count: {len(data)}")
        if len(data) > 0:
            print("First item sample:")
            print(json.dumps(data[0], indent=2))
    else:
        print(f"Error: {response.data}")

    # Debug Technicians List
    print("\n--- Debugging /api/technicians/list/ ---")
    response = client.get('/api/technicians/list/')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Count: {len(data)}")
        if len(data) > 0:
            print("First item sample:")
            print(json.dumps(data[0], indent=2))
    else:
        print(f"Error: {response.data}")

if __name__ == "__main__":
    debug_endpoints()
