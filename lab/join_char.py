def join_words(user_list, user_string):
    new_word = ''
    for word in user_list:
        if user_list.index(word) != len(user_list)-1:
            new_word += str(word) + user_string
        else:
            new_word += str(word)
    return new_word

print(join_words(['Hisham', 'Moideen'], '1 '))