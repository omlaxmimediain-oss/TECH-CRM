import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.amc.models import Plan

def delete_plans():
    count = Plan.objects.count()
    if count == 0:
        print("No plans found to delete.")
    else:
        Plan.objects.all().delete()
        print(f"Successfully deleted {count} Service Plans.")

if __name__ == '__main__':
    delete_plans()
