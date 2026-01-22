
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.accounts.models import User

def list_users():
    print(f"{'PHONE':<15} | {'ROLE':<12} | {'NAME'}")
    print("-" * 50)
    users = User.objects.all().order_by('-date_joined')[:50]
    for u in users:
        # Try to get name from profile
        name = "N/A"
        if hasattr(u, 'customer_profile'):
            name = u.customer_profile.full_name
        elif hasattr(u, 'technician_profile'):
            name = u.technician_profile.full_name
        elif hasattr(u, 'admin_profile'):
            name = u.admin_profile.full_name
        elif hasattr(u, 'area_lead_profile'):
            name = u.area_lead_profile.full_name
            
        print(f"{u.phone:<15} | {u.role:<12} | {name}")

if __name__ == "__main__":
    list_users()
