 Use regular expressions to extract
 specific types of data, such as email addresses, phone numbers, dates
 (e.g., MM/DD/YYYY format)


import re

def extract_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        phone_pattern = r'\b(?:\d{10}|\d{3}[-\s]?\d{3}[-\s]?\d{4})\b'
        date_pattern = r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([0-9]{4})\b'

        emails = re.findall(email_pattern, content)
        phones = re.findall(phone_pattern, content)
        dates = re.findall(date_pattern, content)
        formatted_dates = [f"{m}/{d}/{y}" for m, d, y in dates]

        print("== Emails ==")
        for email in emails:
            print(email)

        print("\n== Phone Numbers ==")
        for phone in phones:
            print(phone)

        print("\n== Dates (MM/DD/YYYY) ==")
        for date in formatted_dates:
            print(date)

    except FileNotFoundError:
        print(f"File not found: {file_path}")


extract_from_file(r"Give path")
