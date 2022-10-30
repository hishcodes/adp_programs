def is_decimal(user_input):
    decimal_count = 0
    for letter in user_input:
        if ord(letter) in range(48,58):
            decimal_count += 1
    if decimal_count == len(user_input):
        return True
    else:
        return False

print(is_decimal('123679046'))