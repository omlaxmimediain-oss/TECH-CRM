# ETS-911 Backend Setup Instructions

## Setup Steps

1. **Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Copy environment file:**
```bash
copy .env.example .env
```

4. **Update .env with your settings**

5. **Create database:**
```bash
createdb ets911
```

6. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create superuser:**
```bash
python manage.py createsuperuser
```

8. **Run development server:**
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST /api/auth/register/ - Register user
- POST /api/auth/login/ - Login
- POST /api/auth/refresh/ - Refresh token
- GET /api/auth/me/ - Get profile

### Technicians
- POST /api/technicians/toggle-online/ - Toggle online status
- POST /api/technicians/verify-kyc/ - Verify KYC
- GET /api/technicians/profile/ - Get profile

### Tickets
- POST /api/tickets/create/ - Create ticket
- GET /api/tickets/list/ - List tickets
- POST /api/tickets/<id>/accept/ - Accept ticket
- POST /api/tickets/<id>/check-in/ - Check-in with OTP
- POST /api/tickets/<id>/check-out/ - Check-out with OTP
- GET /api/tickets/<id>/otp/ - Get OTP (customer)

### Payouts
- GET /api/payouts/wallet/ - Get wallet
- GET /api/payouts/transactions/ - Get transactions
- POST /api/payouts/deposit/ - Deposit funds
- POST /api/payouts/ratings/create/<ticket_id>/ - Rate ticket
- GET /api/payouts/list/ - List payouts

### AMC
- POST /api/amc/create/ - Create subscription
- GET /api/amc/list/ - List subscriptions

## Docker Setup

```bash
docker-compose up --build
```

## Complete!
All backend code has been generated and is ready to use.
