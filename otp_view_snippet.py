
from .models import PhoneOTP
import random

@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    """Send OTP to phone number"""
    phone = request.data.get('phone')
    if not phone:
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        
    # Generate 6-digit OTP
    otp = str(random.randint(100000, 999999))
    
    # Save/Update OTP
    PhoneOTP.objects.update_or_create(
        phone=phone,
        defaults={'otp': otp, 'attempts': 0}
    )
    
    return Response({
        'message': 'OTP sent successfully',
        'debug_otp': otp 
    })
