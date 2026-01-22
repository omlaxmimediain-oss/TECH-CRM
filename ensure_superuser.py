
import os
import django
import sys

sys.path.append('c:/Users/ADMIN/pro/aanti')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import Customer
User = get_user_model()

def create_admin():
    phone = "9999999999"
    password = "admin123"
    
    try:
        if not User.objects.filter(phone=phone).exists():
            print("Creating superuser...")
            user = User.objects.create_superuser(phone=phone, password=password)
            user.role = 'ADMIN'
            user.save()
            
            # Ensure AdminProfile exists
            from apps.accounts.models import AdminProfile
            if not AdminProfile.objects.filter(user=user).exists():
                AdminProfile.objects.create(
                    user=user,
                    full_name="System Administrator"
                )
            print("Superuser created.")
        else:
            print("Superuser already exists. Resetting password...")
            user = User.objects.get(phone=phone)
            user.set_password(password)
            user.role = 'ADMIN' # Ensure role is ADMIN
            user.save()
            print("Superuser password reset.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    create_admin()
