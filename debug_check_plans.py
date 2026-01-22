import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.amc.models import Plan

def check_plans():
    plans = Plan.objects.all()
    print(f"Total Plans in DB: {plans.count()}")
    
    if plans.count() == 0:
        print("ERROR: No plans found in database! The seed script might have failed.")
    else:
        print("\nExisting Plans:")
        for p in plans:
            print(f"- {p.name} (Code: {p.code}, Category: {p.category}, Active: {p.is_active})")
            
        active_plans = Plan.objects.filter(is_active=True)
        print(f"\nActive Plans (visible via API): {active_plans.count()}")

if __name__ == '__main__':
    check_plans()
