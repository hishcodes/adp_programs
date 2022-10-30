def to_uppercase(words):
    upper_words = ''
    for letter in words:
        if ord(letter) in range(97,123):
            lower_letter_asci = ord(letter)
            upper_letter_asci = lower_letter_asci - 32
            upper_letter = chr(upper_letter_asci)
            upper_words += str(upper_letter)
        else:
            upper_words += letter
    print(upper_words)

to_uppercase("HiShAm")

