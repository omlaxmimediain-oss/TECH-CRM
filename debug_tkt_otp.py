
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tickets.models import Ticket, OTP

try:
    ticket = Ticket.objects.get(ticket_number='TKT-20260109-62C2D4C0')
    print(f"Ticket: {ticket.ticket_number}")
    print(f"Status: {ticket.status}")
    print(f"Technician: {ticket.technician}")
    
    otps = OTP.objects.filter(ticket=ticket).order_by('-created_at')
    print(f"\nFound {otps.count()} OTPs:")
    for otp in otps:
        print(f" - Type: {otp.otp_type}, Code: {otp.otp_code}, Used: {otp.is_used}, Locked: {otp.is_locked}, Expires: {otp.expires_at}")
        
except Ticket.DoesNotExist:
    print("Ticket not found")
