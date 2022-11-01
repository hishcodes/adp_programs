def split_words(words, split_char):
    split_at = split_char
    new_list  = []
    word = ''
    for characters in words:
        if characters != str(split_at):
            word += characters
        else:
            new_list.append(word)
            word = ''
    new_list.append(word)
    return new_list

print(split_words('hello world', ' '))