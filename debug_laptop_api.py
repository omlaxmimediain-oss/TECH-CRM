import os
import django
import json
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.accounts.models import User, Customer
from apps.amc.views import LaptopViewSet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def debug_laptops(phone):
    user = User.objects.get(phone=phone)
    factory = APIRequestFactory()
    view = LaptopViewSet.as_view({'get': 'list'})
    request = factory.get('/api/amc/laptops/')
    force_authenticate(request, user=user)
    response = view(request)
    print(f"User: {user.phone} ({user.role})")
    print(f"Status Code: {response.status_code}")
    print(f"Data: {json.dumps(response.data, indent=2)}")

if __name__ == "__main__":
    debug_laptops('9999999991')
