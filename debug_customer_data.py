import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User, Customer
from apps.payouts.models import Wallet

def check_customers():
    print("Checking Customer Data Integrity...")
    customers = User.objects.filter(role='CUSTOMER')
    print(f"Found {customers.count()} users with role 'CUSTOMER'")

    for user in customers:
        print(f"\nUser: {user.phone} ({user.id})")
        
        # Check Profile
        try:
            profile = user.customer_profile
            print(f"  - Profile: OK ({profile.full_name})")
        except User.customer_profile.RelatedObjectDoesNotExist:
            print("  - Profile: MISSING!")
        except Exception as e:
            print(f"  - Profile: Error ({e})")

        # Check Wallet
        try:
            wallet = Wallet.objects.get(user=user)
            print(f"  - Wallet: OK (Balance: {wallet.balance})")
        except Wallet.DoesNotExist:
            print("  - Wallet: MISSING!")
        except Exception as e:
            print(f"  - Wallet: Error ({e})")

if __name__ == '__main__':
    check_customers()
