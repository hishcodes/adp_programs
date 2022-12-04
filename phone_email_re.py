import re

#Email id validator

def validate_email(email_id):
    email_id_regex = re.compile(r'''(
        [a-zA-Z0-9.]+       #username
        \@                  # @ symbol
        [a-zA-Z0-9]+        #domain name
        \.                  #dot for extension
        [a-zA-Z.]{2,5}      #domain extension
        )''', re.VERBOSE)
    mo = email_id_regex.search(email_id)
    return mo

print(validate_email('info@hishcodes.com'))
print(validate_email('hishcodes@gmail.com'))
print(validate_email('example.in'))

#Phone number validator

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

    return mo

print(validate_phone('123-456-7890'))
print(validate_phone('123.456.7890'))
print(validate_phone('(123)-456-789'))
print(validate_phone('1a2-3b5-8s68'))