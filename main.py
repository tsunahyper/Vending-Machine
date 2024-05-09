
import item

def interface():
    print("""
        ------------------------------------
          Welcome to Pokey Vending Machine!
        ------------------------------------
        """)
    print("Please choose a category:")
    print("1. Drinks")
    print("2. Snacks")
    print("3. Exit")
    print("Please enter your choice: ")
    choice = int(input())
    if choice == 1:
        total_drink = displaydrinks()
    elif choice == 2:
        pass
        # displaysnacks()
    elif choice == 3:
        exit()
    else:
        print("Please enter a valid choice")
        interface()
    
def displaydrinks():
    choose_drink = []
    get_drinks = item.option[0]["Drinks"]
    print(get_drinks)
    for i in get_drinks:
        print(f"{i['ItemID']}. {i['ItemName']} - ${i['ItemPrice']}")
    print("Please enter your choice: ")
    choice = int(input())
    choose_drink.append(get_drinks[choice-1])
    if choice == 111:
        print("You have selected Coca Cola")
    elif choice == 112:
        print("You have selected Mineral Water")
    elif choice == 113:
        print("You have selected Mountain Dew")
    elif choice == 114:
        print("You have selected Soya Bean")
    elif choice == 115:
        print("You have selected Justea Peach")
    else:
        print("Please enter a valid choice")
        displaydrinks()
    print("Would you like to add another item?")
    print("1. Yes")
    print("2. No")
    print("Please enter your choice: ")
    choice = int(input())
    if choice == 1:
        displaydrinks()
    elif choice == 2:
        interface()
    else:
        print("Please enter a valid choice")
        displaydrinks()
    return (choose_drink)
    
        