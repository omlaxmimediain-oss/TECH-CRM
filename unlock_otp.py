import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tickets.models import Ticket, OTP

def unlock_otp(otp_id):
    try:
        otp = OTP.objects.get(id=otp_id)
        otp.is_locked = False
        otp.attempt_count = 0
        otp.save()
        print(f"OTP {otp_id} unlocked and attempts reset.")
    except OTP.DoesNotExist:
        print(f"OTP {otp_id} not found.")

if __name__ == "__main__":
    # OTP ID from previous debug output
    unlock_otp('43bc149b-eeda-4a73-b8e1-f46c130a24a7')
