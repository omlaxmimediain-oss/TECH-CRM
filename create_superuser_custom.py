import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User, AdminProfile

def create_superadmin():
    phone = '9999999999'
    password = 'admin123'
    
    # Check if user exists
    if User.objects.filter(phone=phone).exists():
        print(f"User with phone {phone} already exists.")
        user = User.objects.get(phone=phone)
        # Update password just in case
        user.set_password(password)
        user.role = 'ADMIN'
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Updated existing user credentials and permissions.")
    else:
        print(f"Creating new superadmin with phone {phone}...")
        user = User.objects.create_superuser(
            phone=phone,
            password=password,
            role='ADMIN'
        )
        print("User created successfully.")

    # Ensure AdminProfile exists
    if not hasattr(user, 'admin_profile'):
        print("Creating AdminProfile...")
        AdminProfile.objects.create(
            user=user,
            full_name="Super Admin"
        )
        print("AdminProfile created.")
    else:
        print("AdminProfile already exists.")

if __name__ == '__main__':
    try:
        create_superadmin()
        print("Superadmin setup complete.")
    except Exception as e:
        print(f"Error: {e}")
