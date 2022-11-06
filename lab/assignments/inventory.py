inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for key,value in inventory.items():
        print(str(value) + " " + str(key))
        total_items += value
    print('Total number of items: '+ str(total_items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

displayInventory(inventory)
addToInventory(inventory, addedItems)
displayInventory(inventory)