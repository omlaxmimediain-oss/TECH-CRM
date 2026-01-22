
import os
import django
import sys
from decimal import Decimal

# Setup Django environment
sys.path.append('c:\\Users\\ADMIN\\pro\\aanti')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tickets.serializers import CreateTicketSerializer
from apps.accounts.models import User, Customer
from apps.tickets.models import Ticket

def test_ticket_creation():
    print("Testing ticket creation logic...")
    
    # ensure a customer exists
    user, created = User.objects.get_or_create(email='testcustomer@example.com', defaults={'role': 'CUSTOMER', 'phone': '1234567890'})
    if created:
        user.set_password('password123')
        user.save()
        Customer.objects.create(user=user)
    else:
        # Check if customer profile exists, create if not
        try:
            user.customer_profile
        except Exception:
             Customer.objects.create(user=user)
    
    customer = user.customer_profile
    print(f"Using customer: {user.email}")

    data = {
        'issue_description': 'Test Issue',
        'location_address': '123 Test St',
        'location_latitude': 28.6139,
        'location_longitude': 77.2090,
        'job_value': 500,
        'is_emergency': False
    }
    
    serializer = CreateTicketSerializer(data=data)
    if serializer.is_valid():
        print("Serializer is valid.")
        try:
            ticket = Ticket.objects.create(
                customer=customer,
                **serializer.validated_data
            )
            print(f"Ticket created successfully: {ticket.ticket_number}")
        except Exception as e:
            print(f"Failed to create ticket: {e}")
    else:
        print(f"Serializer errors: {serializer.errors}")

if __name__ == "__main__":
    test_ticket_creation()
