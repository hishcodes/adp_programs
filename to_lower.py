def to_lowercase(words):
    lower_case_words = ''
    for letter in words:
        if ord(letter) in range(65,91):
            upper_letter_asci = ord(letter)
            lower_letter_asci = upper_letter_asci + 32
            lower_letters = chr(lower_letter_asci)
            lower_case_words += lower_letters
        else:
            lower_case_words += letter
    print(lower_case_words)

to_lowercase('HiShAm')