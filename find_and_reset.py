
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.accounts.models import Customer, User

def find_user_by_name(name_fragment):
    print(f"Searching for customers with name like '{name_fragment}'...")
    customers = Customer.objects.filter(full_name__icontains=name_fragment)
    
    if not customers.exists():
        print("No customers found.")
        # Try checking Users directly just in case the name is stored differently or it's not a customer profile yet
        return

    for c in customers:
        print(f"Found: Name={c.full_name}, Phone={c.user.phone}, Role={c.user.role}")
        # Auto-reset if exact match on fragment to save time
        if name_fragment.lower() in c.full_name.lower():
             print(f"Resetting password for {c.user.phone}...")
             c.user.set_password("Test@123")
             c.user.save()
             print(f"Password reset to 'Test@123'")

if __name__ == "__main__":
    find_user_by_name("CustOne")
