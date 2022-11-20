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
    t.write("\n"+str(q_number) + ". What is the capital of "+str(key)+"?\n")    #prints questions
    q_number += 1   #increments question numbers in the output
    correct_answer = value #set current question's answer as correct_answer
    all_options = list(capitals.values()) #store all the answers in all_options
    all_options.remove(correct_answer)  #remove the correct_answer from all_options
    wrong_options = all_options #store the list of wrong options in wrong_options
    printable_options = random.sample(wrong_options, 3) #randomly pick 3 wrong options
    printable_options = printable_options + [correct_answer]    #add correct answer to the list of wrong answers
    random.shuffle(printable_options)   #shuffle the 4 options

    t.write("a. "+ str(printable_options[0]) +" b. "+str(printable_options[1])+" c. "+ str(printable_options[2])+" d. "+ str(printable_options[3]))