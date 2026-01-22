
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.accounts.models import User

def reset_password(phone, new_pass="Test@123"):
    try:
        user = User.objects.get(phone=phone)
        user.set_password(new_pass)
        user.save()
        print(f"[SUCCESS] Password for {phone} ({user.role}) reset to: {new_pass}")
    except User.DoesNotExist:
        print(f"[ERROR] User with phone {phone} NOT FOUND.")

if __name__ == "__main__":
    print("--- Resetting Test Account Passwords ---")
    reset_password("6666666666") # Raju
    reset_password("9999999991") # CustOne
