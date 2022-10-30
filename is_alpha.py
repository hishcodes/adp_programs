def is_alpha(words):
    alpha_count = 0
    for letter in words:
        if ord(letter) in range(97,123):
            alpha_count += 1
        elif ord(letter) in range(65,91):
            alpha_count += 1
    if alpha_count == len(words):
        return True
    else:
        return False

print(is_alpha('z'))