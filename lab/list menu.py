def insert(value):
    return L.append(value)

L = []

while(1):
    print("MENU \n 1.Insert \n 2.Update \n 3.Delete \n 4.Select \n 5.Exit")
    choice = str(print("Enter a choice: "))
    
    if(choice == 1):
        value = int(input("Enter a value"))
        insert(value)

