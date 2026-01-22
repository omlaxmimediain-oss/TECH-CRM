import os
import django
import json
from apps.tickets.models import Ticket

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def debug_ticket():
    ticket_number = 'TKT-20260110-54804E93' # Try without the #
    try:
        t = Ticket.objects.get(ticket_number=ticket_number)
        print(f"Ticket Found: {t.ticket_number}")
        print(f"Issue Description: {t.issue_description}")
        print(f"Location Address: {t.location_address}")
        print(f"Location Latitude: {t.location_latitude}")
        print(f"Location Longitude: {t.location_longitude}")
        print(f"Status: {t.status}")
    except Ticket.DoesNotExist:
        # Try with #
        try:
            t = Ticket.objects.get(ticket_number='#' + ticket_number)
            print(f"Ticket Found: {t.ticket_number}")
            print(f"Issue Description: {t.issue_description}")
            print(f"Location Address: {t.location_address}")
        except Ticket.DoesNotExist:
            print(f"Ticket {ticket_number} not found!")

if __name__ == "__main__":
    debug_ticket()
