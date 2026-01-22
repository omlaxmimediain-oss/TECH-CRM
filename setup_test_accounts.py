import os
import django
import sys

sys.path.append('c:/Users/ADMIN/pro/aanti')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User, Customer
from apps.technicians.models import Technician

# Reset Raju
try:
    raju = User.objects.get(phone='6666666666')
    raju.set_password('password123')
    raju.save()
    print('Raju (6666666666) password reset to password123.')
except User.DoesNotExist:
    print('Error: Raju (6666666666) not found.')

# Handle CustOne
cust_phone = '9999999991'
cust_user, created = User.objects.get_or_create(
    phone=cust_phone,
    defaults={'role': 'CUSTOMER', 'phone_verified': True}
)
cust_user.set_password('password123')
cust_user.save()

if created:
    Customer.objects.create(user=cust_user, full_name='CustOne')
    print(f'CustOne ({cust_phone}) account created with password password123.')
else:
    print(f'CustOne ({cust_phone}) password reset to password123.')

# Verification
from django.contrib.auth import authenticate
raju_auth = authenticate(phone='6666666666', password='password123')
cust_auth = authenticate(phone='9999999991', password='password123')

print(f'\nVerification Results:')
print(f'Raju Authenticated: {bool(raju_auth)}')
print(f'CustOne Authenticated: {bool(cust_auth)}')
