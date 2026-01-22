#!/usr/bin/env python
"""
Script to add sample laptop assets for a customer
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import Customer
from apps.amc.models import Laptop

def add_sample_laptops():
    """Add sample laptops for customers who don't have any"""
    
    # Get all customers without laptops
    customers = Customer.objects.all()
    
    for customer in customers:
        laptop_count = Laptop.objects.filter(customer=customer).count()
        
        if laptop_count == 0:
            print(f"\n📱 Adding laptops for customer: {customer.full_name}")
            
            # Add 2 sample laptops
            laptops_data = [
                {
                    'asset_tag': f'LP-{customer.id.hex[:6].upper()}-001',
                    'brand': 'Dell',
                    'model_name': 'Latitude 7490',
                    'serial_number': f'DL{customer.id.hex[:10].upper()}',
                    'processor': 'Intel Core i5-8350U',
                    'ram': '16GB DDR4',
                    'storage': '512GB SSD',
                    'os': 'Windows 11 Pro',
                    'notes': 'Primary work laptop'
                },
                {
                    'asset_tag': f'LP-{customer.id.hex[:6].upper()}-002',
                    'brand': 'HP',
                    'model_name': 'EliteBook 840 G8',
                    'serial_number': f'HP{customer.id.hex[:10].upper()}',
                    'processor': 'Intel Core i7-1165G7',
                    'ram': '32GB DDR4',
                    'storage': '1TB NVMe SSD',
                    'os': 'Windows 11 Pro',
                    'notes': 'Secondary development laptop'
                }
            ]
            
            for laptop_data in laptops_data:
                laptop = Laptop.objects.create(
                    customer=customer,
                    **laptop_data
                )
                print(f"  ✅ Created: {laptop.asset_tag} - {laptop.brand} {laptop.model_name}")
        else:
            print(f"✓ {customer.full_name} already has {laptop_count} laptop(s)")

if __name__ == '__main__':
    print("=" * 60)
    print("Adding Sample Laptop Assets for Customers")
    print("=" * 60)
    add_sample_laptops()
    print("\n✅ Done!")
