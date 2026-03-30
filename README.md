# 🚂 Food on Train

A web application that allows train passengers to order food from restaurants at upcoming stations and get it delivered directly to their seat.

<img width="1917" height="908" alt="image" src="https://github.com/user-attachments/assets/5d4220d8-bfab-45e8-8d41-af661ba108fd" />

<img width="1897" height="904" alt="Screenshot 2024-11-23 161013" src="https://github.com/user-attachments/assets/8f28e224-9f03-4c52-87c5-30e820f8263b" />

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Installation & Setup](#installation--setup)
7. [Running the Application](#running-the-application)
8. [Application Flow](#application-flow)
9. [Routes Reference](#routes-reference)
10. [Supported Trains & Stations](#supported-trains--stations)
11. [Payment Methods](#payment-methods)
12. [OTP Email Verification](#otp-email-verification)
13. [Form Validations](#form-validations)

---

## Project Overview

Food on Train is a Flask-based web application that enables passengers to:
- Enter their train number and view train details
- Select an upcoming station to order food from
- Browse restaurants and their menus at that station
- Add items to cart and manage quantities
- Pay via UPI or Debit Card
- Receive OTP on email to confirm the order
- Get food delivered to their seat

---

## Features

- Train lookup by 5-digit train number
- Station selection from the train's route
- Restaurant listing with a live ratings bar chart (matplotlib)
- Full menu browsing with food images and prices (in ₹)
- Cart management — add, update, and delete items
- Seat number and travel date input before checkout
- Two payment options: UPI and Debit Card
- OTP-based email verification with a 30-second countdown timer
- Client-side form validation on all input forms
- Responsive UI with inline CSS styling

---

## Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Flask           |
| Frontend   | HTML, CSS, JavaScript   |
| Templating | Jinja2                  |
| Email      | Flask-Mail (Gmail SMTP) |
| Charts     | Matplotlib              |
| Data Store | In-memory Python dicts  |

---

## Project Structure

```
project_(FOOD ON TRAIN)_FINAL/
│
├── app.py                  # Main Flask application, all routes
├── database.py             # In-memory data: trains, restaurants, menus
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── index.html          # Train number entry + train details + station selection
│   ├── stations.html       # Station selection (standalone page)
│   ├── restaurants.html    # Restaurant list + ratings bar chart
│   ├── menu.html           # Food menu for a selected restaurant
│   ├── cart.html           # Cart with seat/date input and total bill
│   ├── bill.html           # Alternate cart/bill view
│   ├── payment.html        # Payment method selection (UPI / Card)
│   ├── upi_payment.html    # UPI ID + email form
│   ├── card_payment.html   # Card number, expiry, CVV + email form
│   └── verify.html         # OTP entry with countdown timer
│
└── static/
    └── images/             # Food item images used in menus
        ├── biryani.jpg
        ├── burger.jpg
        ├── chickenbir.jpg
        ├── curry.jpg
        ├── friedrice.jpg
        ├── masala.jpg
        ├── parota.jpg
        ├── pasta.jpg
        ├── tandoori.jpg
        ├── imag1.jpg
        ├── mini1.jpg ... mini9.jpg
        └── css/
```

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Gmail account with an App Password enabled (for OTP emails)

---

## Installation & Setup

**Step 1 — Clone or download the project**

```bash
git clone <repository-url>
cd "project_(FOOD ON TRAIN)_FINAL"
```

**Step 2 — Create and activate a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Configure Gmail for OTP emails**

In `app.py`, update the mail configuration with your Gmail credentials:

```python
app.config["MAIL_USERNAME"] = "your_email@gmail.com"
app.config["MAIL_PASSWORD"] = "your_app_password"   # Gmail App Password
```

> To generate a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords

---

## Running the Application

```bash
python app.py
```

The app runs in debug mode by default. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Application Flow

```
Step 1: Enter Train Number (5-digit)
            ↓
Step 2: View Train Details → Select Station
            ↓
Step 3: Browse Restaurants at Station + View Ratings Chart
            ↓
Step 4: View Menu → Add Items to Cart
            ↓
Step 5: Review Cart → Enter Seat Number & Travel Date
            ↓
Step 6: Select Payment Method (UPI or Debit Card)
            ↓
Step 7: Enter Payment Details + Email
            ↓
Step 8: Receive OTP on Email → Enter OTP (30-second window)
            ↓
Step 9: Order Confirmed → Food delivered to seat
```

---

## Routes Reference

| Method | Route                        | Description                              |
|--------|------------------------------|------------------------------------------|
| GET    | `/`                          | Home page — train number entry form      |
| POST   | `/`                          | Submit train number, show train details  |
| POST   | `/stations/<train_number>`   | Select station, redirect to restaurants  |
| GET    | `/stations/<train_number>`   | Return station list as JSON              |
| GET    | `/restaurants/<station_code>`| List restaurants + ratings bar chart     |
| GET    | `/menu/<restaurant_id>`      | Show menu for a restaurant               |
| POST   | `/add_to_cart`               | Add a food item to the session cart      |
| GET    | `/cart`                      | View cart with total bill                |
| POST   | `/delete_from_cart`          | Remove or reduce item quantity in cart   |
| GET    | `/payment`                   | Payment method selection page            |
| GET/POST | `/upi_payment`             | UPI payment form + trigger OTP           |
| GET/POST | `/card_payment`            | Card payment form + trigger OTP          |
| GET/POST | `/verify_email`            | OTP entry and verification               |
| POST   | `/validate`                  | Validate submitted OTP                   |
| GET    | `/images/<filename>`         | Serve static food images                 |

---

## Supported Trains & Stations

| Train No. | Train Name          | From                  | To                          | Food Stations                                          |
|-----------|---------------------|-----------------------|-----------------------------|--------------------------------------------------------|
| 12354     | Charminar Express   | Hyderabad Deccan      | Tambaram                    | Secunderabad Junction, Warangal, Vijayawada Junction   |
| 17260     | Telangana Express   | Secunderabad Junction | New Delhi                   | Kazipet Junction, Nagpur Junction, Gwailor Junction    |
| 19045     | Kerala Express      | New Delhi             | Thiruvananthapuram Central  | Kharagpur Junction, Bhubaneswar, Chennai Central       |

Each station has 2–3 restaurants, each with 8–9 menu items ranging from ₹49 to ₹399.

---

## Payment Methods

### UPI Payment
- Enter a valid UPI ID (format: `username@bankname`)
- Enter your email address to receive OTP
- Validated client-side before submission

### Debit Card Payment
- Enter a 16-digit card number
- Enter expiry date in `MM/YY` format (must be a future date)
- Enter a 3-digit CVV (toggle show/hide supported)
- Enter your email address to receive OTP
- All fields validated client-side before submission

---

## OTP Email Verification

- After payment details are submitted, a 6-digit OTP is generated and sent to the provided email via Gmail SMTP
- The OTP entry page shows a 30-second countdown timer
- If the timer expires, the submit button is disabled
- On successful OTP match, the order is confirmed and the user is redirected to the home page

---

## Form Validations

| Form          | Validations Applied                                                  |
|---------------|----------------------------------------------------------------------|
| Train Number  | Must be exactly 5 digits                                             |
| Station       | Must select a valid station from the dropdown                        |
| Cart          | Seat/coach field required; travel date must be today or future       |
| UPI Payment   | UPI ID format (`x@y`); valid email format                            |
| Card Payment  | 16-digit card; MM/YY expiry (future); 3-digit CVV; valid email       |
| OTP           | Must be entered within 30 seconds; must match the sent OTP           |
