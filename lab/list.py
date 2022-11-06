import sys

def insert(value):
    return L.append(value)

def update(index, value):
    L[index] = value

def delete(value):
    return L.remove(value)

def select():
    print(L)

L = []

while(1):
    print("MENU \n 1.Insert \n 2.Update \n 3.Delete \n 4.Select \n 5.Exit")
    choice = int(input("Enter a choice: "))

    if(choice == 1):
        value = int(input("Enter a value "))
        insert(value)
        select()

    elif(choice == 2):
        old_value = int(input("Enter the old value: "))
        if(old_value in L):
            old_index = L.index(old_value)
            new_value = int(input("Enter the new value: "))
            update(old_index, new_value)
            select()
        else:
            print("The entered old number does not exist in the list")
            select()

    elif(choice == 3):
        value = int(input("Enter a value to delete"))
        if(value in L):
            delete(value)
            select()
        else:
            print("The entered number does not exist in the list")
            select()

    elif(choice == 4):
        select()

    elif(choice == 5):
        sys.exit()

    else:
        print("Invalid choice")