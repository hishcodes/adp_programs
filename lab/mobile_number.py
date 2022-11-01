def validate_number(phone):
    number_count = 0
    for digits in phone:
        if digits.isnumeric():
            number_count += 1
    if number_count == 10:
        return True
    else:
        return False

num = input("Enter phone number to validate: ")
print(validate_number(num))