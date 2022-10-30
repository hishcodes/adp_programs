def is_alnum(user_input):
    alnum_count = 0
    for letter in user_input:
        if ord(letter) in range(48,58):
            alnum_count += 1
        elif ord(letter) in range(65,91):
            alnum_count += 1
        elif ord(letter) in range(97,123):
            alnum_count += 1
    if alnum_count == len(user_input):
        return True
    else:
        return False

print(is_alnum('skdfhg983'))