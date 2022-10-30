def is_space(user_input):
    space_count = 0
    for character in user_input:
        if ord(character) == ord(' '):
            space_count += 1
    if space_count == len(user_input):
        return True
    else:
        return False

print(is_space('    '))