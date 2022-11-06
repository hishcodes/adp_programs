import sys

def insert(value):
    return L.append(value)

def delete(value):
    return L.remove(value)

def update(index, value):
    L[index] = value

def sort(list_name):
    list_name.sort()

def select():
    print(L)

L = []

while(1):
    print("MENU \n 1.Add \n 2.Delete \n 3.Update \n 4.Search \n 5.Sort \n 6.Exit")
    choice = int(input("Enter a choice: "))

    if(choice == 1):
        value = input("Enter student name: ")
        insert(value)
        select()

    elif(choice == 2):
        value = input("Enter name of the student: ")
        if(value in L):
            delete(value)
            select()
        else:
            print("The entered name does not exist in the list")
            select()

    elif(choice == 3):
        old_value = input("Enter the old name: ")
        if(old_value in L):
            old_index = L.index(old_value)
            new_value = input("Enter the new name: ")
            update(old_index, new_value)
            select()
        else:
            print("The entered old name does not exist in the list")
            select()

    elif(choice == 4):
        value = input("Enter the student name to search: ")
        if value in L:
            value_index = L.index(value)
            print('The student name '+str(value)+' is stored in the list at index '+ str(value_index))
        else:
            print('The entered student name does not exist in the list')

    elif(choice == 5):
        sort(L)
        select()

    elif(choice == 6):
        sys.exit()

    else:
        print("Invalid choice")