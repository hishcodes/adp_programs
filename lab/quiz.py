import random

t = open("quiz.txt", "w")
q_number = 1
capitals = {'Karnataka':'Bangalore',
'Kerala':'Trivendram',
'Andhra Pradesh':'Amaravati',
'Goa':'Panaji',
'Maharashtra':'Mumbai',
'Punjab':'Gandhinagar',
'Sikkim':'Gangtok',
'Madhya Pradesh':'Bhopal',
'Meghalaya':'Shillong',
'Haryana':'Chandigarh'
}

for key,value in capitals.items():
    t.write("\n"+str(q_number) + ". What is the capital of "+str(key)+"?\n")
    q_number += 1
    correct_answer = value
    all_options = list(capitals.values())
    all_options.remove(correct_answer)
    wrong_options = all_options
    printable_options = random.sample(wrong_options, 3)
    printable_options = printable_options + [correct_answer]
    random.shuffle(printable_options)

    t.write("a. "+ str(printable_options[0]) +" b. "+str(printable_options[1])+" c. "+ str(printable_options[2])+" d. "+ str(printable_options[3]))