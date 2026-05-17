# Synthetic Test Data Generator
# Generates fake PHI for demo purposes only

import random
from datetime import datetime, timedelta

# Synthetic patient data - NOT REAL PHI
FIRST_NAMES = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Lisa", "James", "Mary"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
CITIES = ["Boston", "New York", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
STATES = ["MA", "NY", "IL", "TX", "AZ", "PA", "CA"]
DIAGNOSES = [
    "Type 2 Diabetes Mellitus",
    "Hypertension",
    "Asthma",
    "Coronary Artery Disease",
    "Chronic Kidney Disease",
    "COPD",
    "Depression",
    "Osteoarthritis"
]

def generate_ssn():
    """Generate a fake SSN in format XXX-XX-XXXX"""
    # Use 900-999 range which is not assigned to avoid any real SSN collision
    area = random.randint(900, 999)
    group = random.randint(10, 99)
    serial = random.randint(1000, 9999)
    return f"{area}-{group}-{serial}"

def generate_mrn():
    """Generate a fake Medical Record Number"""
    return f"MRN-{random.randint(100000, 999999)}"

def generate_phone():
    """Generate a fake phone number"""
    area = random.randint(200, 999)
    exchange = random.randint(200, 999)
    number = random.randint(1000, 9999)
    return f"{area}-{exchange}-{number}"

def generate_dob():
    """Generate a fake date of birth (age 18-90)"""
    days_ago = random.randint(18*365, 90*365)
    dob = datetime.now() - timedelta(days=days_ago)
    return dob.strftime("%Y-%m-%d")

def generate_address():
    """Generate a fake address"""
    street_num = random.randint(100, 9999)
    streets = ["Main St", "Oak Ave", "Maple Dr", "Park Blvd", "Washington St", "Lincoln Ave"]
    city = random.choice(CITIES)
    state = random.choice(STATES)
    zipcode = random.randint(10000, 99999)
    return f"{street_num} {random.choice(streets)}, {city}, {state} {zipcode}"

def generate_patient():
    """Generate a complete synthetic patient record"""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    
    return {
        "full_name": f"{first_name} {last_name}",
        "ssn": generate_ssn(),
        "date_of_birth": generate_dob(),
        "medical_record_number": generate_mrn(),
        "diagnosis": random.choice(DIAGNOSES),
        "phone_number": generate_phone(),
        "email": f"{first_name.lower()}.{last_name.lower()}@email.com",
        "address": generate_address()
    }

def generate_patients(count=10):
    """Generate multiple synthetic patient records"""
    return [generate_patient() for _ in range(count)]

# Made with Bob
