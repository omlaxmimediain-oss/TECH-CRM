import os
import django
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.accounts.models import User
from apps.tickets.views import list_tickets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def debug_customer_tickets(phone_number):
    try:
        user = User.objects.get(phone=phone_number)
        print(f"User found: {user.phone}, Role: {user.role}")
        
        factory = APIRequestFactory()
        request = factory.get('/api/tickets/list/')
        force_authenticate(request, user=user)
        
        response = list_tickets(request)
        print(f"Status Code: {response.status_code}")
        print(f"Data: {response.data}")
    except User.DoesNotExist:
        print(f"User with phone {phone_number} not found")
    except Exception as e:
        print(f"Error: {e}")

# Replace with the actual phone number you are testing with
# I'll try to find a customer user first
try:
    customer_user = User.objects.filter(role='CUSTOMER').first()
    if customer_user:
        debug_customer_tickets(customer_user.phone)
    else:
        print("No customer users found in DB")
except Exception as e:
    print(f"Setup failed: {e}")
