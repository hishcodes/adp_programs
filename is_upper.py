def is_upper(words):
    upper_count = 0
    for letter in words:
        if ord(letter) in range(65,91):
            upper_count += + 1
    if upper_count == len(words):
        return True
    else:
        return False

print(is_upper('HISHAM'))