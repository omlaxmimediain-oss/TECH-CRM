import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.amc.models import Plan

def create_plans():
    # 1. Delete existing plans (or mark inactive, but user said remove)
    print("Deleting existing plans...")
    Plan.objects.all().delete()

    plans_data = [
        # Residential (Home PC Users)
        {
            "name": "Basic Plan",
            "code": "RES_BASIC",
            "category": "Residential",
            "price": 999,
            "visits": 4,
            "color_theme": "blue",
            "features": [
                "1 PC / Laptop Only (Mira-Bhayander)",
                "Valid for 12 months",
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },
        {
            "name": "Family Plan",
            "code": "RES_FAMILY",
            "category": "Residential",
            "price": 1999,
            "visits": 4,
            "color_theme": "indigo",
            "features": [
                "3 PC / Laptop Only (Mira-Bhayander)",
                "Valid for 12 months",
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },
        {
            "name": "Utility Plan",
            "code": "RES_UTILITY",
            "category": "Residential",
            "price": 4999,
            "visits": 4,
            "color_theme": "purple",
            "features": [
                "6 PC / Laptop (Mira-Bhayander)",
                "Valid for 12 months",
                "Escalated - Data Backup/Recovery & Safety Assistance",
                "Unlimited Remote Assistance (365 Days)*",
                "4 Visit for PC/Laptop Diagnose & Cleaning (Quarterly)*",
                "Thermal Optimization (Liquid Metal or Silicon Paste)",
                "Performance Optimization (Speed Boost, SSD Check, RAM Check)",
                "Cable Management, Peripheral Integration",
                "Printer & Wi-Fi Troubleshooting",
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "System Networking Support",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },
        
        # Commercial (Small Business & MSME's)
        {
            "name": "MSME Business Plan",
            "code": "COM_MSME",
            "category": "Commercial",
            "price": 12000,
            "visits": 6,
            "color_theme": "emerald",
            "features": [
                "UPTO 8 PC/Laptops (Mira-Bhayander)",
                "Valid for 12 months",
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
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },
        {
            "name": "Growth Plan",
            "code": "COM_GROWTH",
            "category": "Commercial",
            "price": 16000,
            "visits": 12,
            "color_theme": "teal",
            "features": [
                "UPTO 12 PC/Laptops (Mira-Bhayander)",
                "Valid for 12 months",
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
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },
        {
            "name": "Premium Plan",
            "code": "COM_PREMIUM",
            "category": "Commercial",
            "price": 20000,
            "visits": 12,
            "color_theme": "cyan",
            "features": [
                "UPTO 18 PC/Laptops (Mira-Bhayander)",
                "Valid for 12 months",
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
                "Opeating System Assistance (Windows/Mac/Linux)",
                "Virus/Malware Removal & Firewall Integration",
                "Discounted Rates on Hardware (Up to 20%)"
            ]
        },

        # Industrial (Corporates & Enterprises)
        {
            "name": "Standard IT Support Plan",
            "code": "IND_STANDARD",
            "category": "Industrial",
            "price": 35000,
            "visits": 12,
            "color_theme": "orange",
            "features": [
                "Up to 30 PCs & 1 Server (Mira-Bhayander)",
                "Valid for 12 months",
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
            ]
        },
        {
            "name": "Advanced IT Plan",
            "code": "IND_ADVANCED",
            "category": "Industrial",
            "price": 50000,
            "visits": 18,
            "color_theme": "red",
            "features": [
                "Up to 50 PCs & 2 Servers (Mira-Bhayander)",
                "Valid for 12 months",
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
            ]
        },
        {
            "name": "Enterprise Plan",
            "code": "IND_ENTERPRISE",
            "category": "Industrial",
            "price": 80000,
            "visits": 24,
            "color_theme": "rose",
            "features": [
                "For 100+ PCs, Custom IT Needs (Mira-Bhayander)",
                "Valid for 12 months",
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
            ]
        }
    ]

    print(f"Creating {len(plans_data)} new plans...")
    for data in plans_data:
        Plan.objects.create(**data)
        print(f"Created: {data['name']}")

    print("All plans created successfully.")

if __name__ == "__main__":
    create_plans()
