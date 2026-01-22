import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tickets.models import Ticket, OTP

def debug_otp(ticket_number):
    try:
        ticket = Ticket.objects.get(ticket_number=ticket_number)
        print(f"Ticket: {ticket.ticket_number} (ID: {ticket.id})")
        print(f"Status: {ticket.status}")
        
        otps = OTP.objects.filter(ticket=ticket).order_by('-created_at')
        if not otps.exists():
            print("No OTPs found for this ticket.")
            return

        for otp in otps:
            print(f"\nOTP ID: {otp.id}")
            print(f"Type: {otp.otp_type}")
            print(f"Code: {otp.otp_code} (Type: {type(otp.otp_code)})")
            print(f"Attempt Count: {otp.attempt_count}")
            print(f"Is Locked: {otp.is_locked}")
            print(f"Is Used: {otp.is_used}")
            print(f"Expires At: {otp.expires_at}")
            
    except Ticket.DoesNotExist:
        print(f"Ticket {ticket_number} not found.")

if __name__ == "__main__":
    debug_otp('TKT-20260109-62C2D4C0')
