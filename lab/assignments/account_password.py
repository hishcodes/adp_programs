import sys
import pyperclip

password={'gmail':'#pass123','yahoo':'secure@0809'}
acc=sys.argv[1]

if acc in password:
    pyperclip.copy(password[acc])
else:
    print("Password does not exist")