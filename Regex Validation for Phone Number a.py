Regex Validation for Phone Number and Email 19

import re 
phone = input("Enter phone number: ") 
email = input("Enter email address: ") 
phone_pattern = r'^\d{10}$' 
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
if re.match(phone_pattern, phone): 
    print("Valid phone number") 
else: 
    print("Invalid phone number") 
if re.match(email_pattern, email): 
    print("Valid email") 
else: 
    print("Invalid email") 