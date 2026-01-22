import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tickets.models import Ticket, OTP
from django.utils import timezone

try:
    ticket = Ticket.objects.get(ticket_number='TKT-20260109-62C2D4C0')
    print(f"Ticket: {ticket.ticket_number}")
    print(f"Status: {ticket.status}")
    print(f"Customer: {ticket.customer}")
    
    # Check what OTP type should exist
    if ticket.status == 'ACCEPTED':
        expected_type = 'CHECK_IN'
    elif ticket.status == 'IN_PROGRESS':
        expected_type = 'CHECK_OUT'
    elif ticket.status == 'PAUSED':
        expected_type = 'RESUME'
    else:
        expected_type = None
        
    print(f"\nExpected OTP Type: {expected_type}")
    
    # Check for active OTPs
    active_otps = OTP.objects.filter(ticket=ticket, is_used=False).order_by('-created_at')
    print(f"\nActive (unused) OTPs: {active_otps.count()}")
    for otp in active_otps:
        is_valid = otp.expires_at > timezone.now()
        print(f"  - Type: {otp.otp_type}, Code: {otp.otp_code}, Valid: {is_valid}, Expires: {otp.expires_at}")
        
    # Check if expected OTP exists
    if expected_type:
        try:
            expected_otp = OTP.objects.filter(
                ticket=ticket,
                otp_type=expected_type,
                is_used=False
            ).latest('created_at')
            print(f"\nFound {expected_type} OTP: {expected_otp.otp_code}")
        except OTP.DoesNotExist:
            print(f"\n❌ NO {expected_type} OTP FOUND - This is the problem!")
            print("Creating one now...")
            from apps.tickets import services
            new_otp = services.create_otp(ticket, expected_type)
            print(f"✅ Created {expected_type} OTP: {new_otp.otp_code}")
        
except Ticket.DoesNotExist:
    print("Ticket not found")
