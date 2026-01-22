import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import Customer, AdminProfile
from apps.technicians.models import Technician

def populate_customers():
    print("Populating Customers...")
    customers = Customer.objects.filter(member_id__isnull=True).order_by('created_at')
    for i, customer in enumerate(customers, 1):
        customer.member_id = f"ETS-{i:03d}"
        customer.save()
        print(f"Updated {customer.full_name} -> {customer.member_id}")

def populate_technicians():
    print("\nPopulating Technicians...")
    technicians = Technician.objects.filter(member_id__isnull=True).order_by('created_at')
    for i, tech in enumerate(technicians, 1):
        tech.member_id = f"ETS-TEC-{i:03d}"
        tech.save()
        print(f"Updated {tech.full_name} -> {tech.member_id}")

def populate_admins():
    print("\nPopulating Admins...")
    # Get all admins, but specifically those needing update to 3-digit format
    admins = AdminProfile.objects.all().order_by('created_at')
    for i, admin in enumerate(admins, 1):
        new_id = f"ETS-ADMIN-{i:03d}"
        if admin.member_id != new_id:
            admin.member_id = new_id
            admin.save()
            print(f"Updated {admin.full_name} -> {admin.member_id}")
        else:
            print(f"Skipping {admin.full_name} (already {admin.member_id})")

if __name__ == "__main__":
    populate_customers()
    populate_technicians()
    populate_admins()
    print("\nPopulation complete!")
