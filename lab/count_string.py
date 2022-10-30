words = 'hisham'
alphabets = {}

# for letters in words:
#     if letters in alphabets:
#         alphabets[letters] = alphabets[letters] + 1
#     else:
#         alphabets[letters] = 1

for letters in words:
    alphabets.setdefault(letters, 0)
    alphabets[letters] = alphabets[letters] + 1

print(alphabets)