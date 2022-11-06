def arrange(user_list):
    x = 0
    y = ''
    while((x<=len(user_list)) and (len(user_list)>1)):
        if(x < len(user_list)-1):
            y = y + user_list[x] + ', '
            x = x + 1
        else:
            y = y + "and " + user_list[len(user_list)-1]
            return y

user_list = ['apples', 'bananas', 'tofu', 'cats']

print(arrange(user_list))