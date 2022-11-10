import re

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


user_email_id = input("Enter your email id: ")
print(validate_email(user_email_id))