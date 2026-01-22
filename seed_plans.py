import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.amc.models import Plan

def seed_plans():
    print("Clearing existing plans...")
    Plan.objects.all().delete()

    plans_data = [
        # --- Residential (Home Users) ---
        {
            "name": "Basic Plan",
            "code": "RES_BASIC",
            "category": "Residential",
            "price": 999.00,
            "visits": 4,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": False,
            "description": "1 PC / Laptop Only (Mira-Bhayander)"
        },
        {
            "name": "Family Plan",
            "code": "RES_FAMILY",
            "category": "Residential",
            "price": 1999.00,
            "visits": 4,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": False,
            "description": "3 PC / Laptop Only (Mira-Bhayander)"
        },
        {
            "name": "Utility Plan",
            "code": "RES_UTILITY",
            "category": "Residential",
            "price": 4999.00,
            "visits": 4,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "System Networking Support",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": True,
            "description": "6 PC / Laptop (Mira-Bhayander)"
        },
        
        # --- Commercial (Enterprises & MSMEs) ---
        {
            "name": "MSME Business Plan",
            "code": "COM_MSME",
            "category": "Commercial",
            "price": 12000.00,
            "visits": 6,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "6 Visit for PC/Laptop Diagnose & Cleaning*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer, Scanner & Peripheral Support",
                "Virus & Security Scan Support",
                "Network & Wi-Fi Optimization",
                "Cloud Backup Setup & Data Recovery Guidance",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": False,
            "description": "UPTO 8 PC/Laptops (Mira-Bhayander)"
        },
        {
            "name": "Growth Plan",
            "code": "COM_GROWTH",
            "category": "Commercial",
            "price": 16000.00,
            "visits": 12,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "12 Visit for PC/Laptop Diagnose & Cleaning*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer, Scanner & Peripheral Support",
                "Virus & Security Scan Support",
                "Network & Wi-Fi Optimization",
                "Cloud Backup Setup & Data Recovery Guidance",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": True,
            "description": "UPTO 12 PC/Laptops (Mira-Bhayander)"
        },
        {
            "name": "Premium Plan",
            "code": "COM_PREMIUM",
            "category": "Commercial",
            "price": 20000.00,
            "visits": 12,
            "color_theme": "red",
            "features": [
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "12 Visit for PC/Laptop Diagnose & Cleaning (Yearly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer, Scanner & Peripheral Support",
                "Virus & Security Scan Support",
                "Network & Wi-Fi Optimization",
                "Cloud Backup Setup & Data Recovery Guidance",
                "Operating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ],
            "best_value": False,
            "description": "UPTO 18 PC/Laptops (Mira-Bhayander)"
        },

        # --- Industrial (Corporates & Enterprises) ---
        {
            "name": "Standard IT Support Plan",
            "code": "IND_STANDARD",
            "category": "Industrial",
            "price": 35000.00,
            "visits": 12,
            "color_theme": "red",
            "features": [
                "Priority IT Support Team",
                "Bi-Weekly Preventive Maintenance Visits (12 Visits a Year)",
                "During Working Hrs. Emergency Support (Onsite & Remote)",
                "Server Management & Data Backup Solutions",
                "Enterprise Antivirus & Endpoint Security",
                "Email Server & Cloud Management Google Workspace, Office 360",
                "Firewall & Network Security Support",
                "Printer & Scanner Fleet Management",
                "Annual IT Health Check Reports & Consultation",
                "Discounted IT Infrastructure Upgrades"
            ],
            "best_value": False,
            "description": "Up to 30 PCs & 1 Server (Mira-Bhayander)"
        },
        {
            "name": "Advanced IT Plan",
            "code": "IND_ADVANCED",
            "category": "Industrial",
            "price": 50000.00,
            "visits": 18,
            "color_theme": "red",
            "features": [
                "Priority IT Support Team",
                "Bi-Weekly Preventive Maintenance Visits (18 Visits a Year)",
                "During Working Hrs. Emergency Support (Onsite & Remote)",
                "Server Management & Data Backup Solutions",
                "Enterprise Antivirus & Endpoint Security",
                "Email Server & Cloud Management Google Workspace, Office 360",
                "Firewall & Network Security Support",
                "Printer & Scanner Fleet Management",
                "Annual IT Health Check Reports & Consultation",
                "Discounted IT Infrastructure Upgrades"
            ],
            "best_value": True,
            "description": "Up to 50 PCs & 2 Servers (Mira-Bhayander)"
        },
        {
            "name": "Enterprise Plan",
            "code": "IND_ENTERPRISE",
            "category": "Industrial",
            "price": 80000.00,
            "visits": 24,
            "color_theme": "red",
            "features": [
                "Dedicated IT Support Team",
                "Bi-Weekly Preventive Maintenance Visits (24 Visits a Year)",
                "During Working Hrs. Emergency Support (Onsite & Remote)",
                "Server Management & Data Backup Solutions",
                "Enterprise Antivirus & Endpoint Security",
                "Email Server & Cloud Management Google Workspace, Office 360",
                "Firewall & Network Security Support",
                "Printer & Scanner Fleet Management",
                "Annual IT Health Check Reports & Consultation",
                "Discounted IT Infrastructure Upgrades"
            ],
            "best_value": False,
            "description": "For 100+ PCs, Custom IT Needs (Mira-Bhayander)"
        },
    ]

    for p in plans_data:
        # We store the description (PC count) as the first feature or just assume frontend maps it. 
        # But wait, the frontend currently hardcodes checks like "p.code === 'COM_MSME'".
        # To make it data-driven, let's insert the description as a special feature or just update the logic.
        # However, the Plan model doesn't have a 'description' field.
        # I'll update the frontend to specifically look for these Plan Codes and print the text, 
        # OR I can prepend it to features? No, that looks bad.
        # I'll stick to the frontend mapping for the description line to keep the UI clean.
        
        plan = Plan.objects.create(
            name=p['name'],
            code=p['code'],
            category=p['category'],
            price=p['price'],
            visits=p['visits'],
            color_theme=p['color_theme'],
            features=p['features']
        )
        print(f"Created plan: {plan.name}")

if __name__ == '__main__':
    seed_plans()
