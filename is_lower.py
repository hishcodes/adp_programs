def is_upper(words):
    lower_count = 0
    for letter in words:
        if ord(letter) in range(97,123):
            lower_count += 1
    if lower_count == len(words):
        return True
    else:
        return  False

print(is_upper('hisham'))