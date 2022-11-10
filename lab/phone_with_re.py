import re

def validate_phone(phone):
    phone_regex = re.compile(r'''(
        (\d{3})?            #optional 1st 3 digits
        (-|\.)              #symbols
        \d{3}               #2nd 3 digits
        (-|\.)              #symbols
        \d{4}               #4 digits
        (\s(ext|ext\.|x)\s  #optional extension
        \d{1,5})?           #optional extension digits
        )''', re.VERBOSE)
        
    mo = phone_regex.search(phone)

    if mo != None:
        return True
    else:
        return False

number = input("Enter a phone number: ")

if validate_phone(number) == True:
    print("valid phone number")
else:
    print("invalid phone number")