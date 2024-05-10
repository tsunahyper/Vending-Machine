import os
import item

def interface(*args):
    choose_drink = []
    choose_snacks = []
    os.system('clear')
    if args:
        total_drink = args[0]
        total_snacks = args[1] if len(args) > 1 else []
    else:
        total_drink = []
        total_snacks = []
    total_price= 0
    print("""
        ------------------------------------
          Welcome to Tsuna's Vending Machine!
        ------------------------------------
        """)
    print("Please choose a category:")
    print("(1) Drinks")
    print("(2) Snacks")
    print("(3) Payment")
    print("(0) Exit")
    print("\nPlease enter your choice: ")
    choice = int(input())
    if choice == 1:
        displaydrinks(choose_drink)
    elif choice == 2:
        displaysnacks(choose_snacks,total_drink)
    elif choice == 3:
        total_price = calculate_total(total_drink, total_snacks)
        print(f"\nTotal price: ${total_price}")
        print("\nThank you for shopping with us!")
        print("------------------------------------")
        print("\nWould you like a receipt?\n")
        print("(1) Yes")
        print("(2) No")
        print("\nPlease enter your choice: ")
        choice = int(input())
        if choice == 1:
            os.system('clear')
            print("""
            ------------------------------------
                            Receipt
            ------------------------------------
            """)
            print("DRINKS:\n")
            for drink_id in total_drink:
                for drink in item.option[0]["Drinks"]:
                    if drink["ItemID"] == drink_id:
                        print(f"-> {drink['ItemName']}: ${drink['ItemPrice']}")
            print("\nSNACKS:\n")
            for snack_id in total_snacks:
                for snack in item.option[1]["Snacks"]:
                    if snack["ItemID"] == snack_id:
                        print(f"-> {snack['ItemName']}: ${snack['ItemPrice']}")
            print(f"\nTotal price: ${total_price}")
            print("\nThank you for shopping and purchasing items from Tsuna's Vending Machine! Have a nice Day!")
        elif choice == 2:
            print("You will be redirected back to the main menu")  
            interface()
        else:
            print("Please enter a valid choice")
            interface()
    elif choice == 0:
        exit()
    else:
        print("Please enter a valid choice")
        interface()



def displaydrinks(choose_drink):
    get_drinks = item.option[0]["Drinks"]
    os.system('clear')
    for i in get_drinks:
        print(f"({i['ItemID']}) {i['ItemName']} - ${i['ItemPrice']}")
    print("\n(0) Back to main menu")
    print("\n\nPlease enter your choice: ")
    choice = int(input())
    if choice in [111, 112, 113, 114, 115]:
        choose_drink.append(choice)
        print(f"You have selected {get_drinks[choice - 111]['ItemName']}")
    elif choice == 0:
        print("You will be redirected back to the main menu")
        interface()
    else:
        print("Please enter a valid choice")
        displaydrinks(choose_drink)
    os.system('clear')
    print("Would you like to add another item?")
    print("(1) Yes")
    print("(2) No")
    print("Please enter your choice: ")
    choice = int(input())
    if choice == 1:
        displaydrinks(choose_drink)
    elif choice == 2:
        interface(choose_drink)
    else:
        print("Please enter a valid choice")
        displaydrinks(choose_drink)
    


def displaysnacks(choose_snacks, total_drink):
    get_snacks = item.option[1]["Snacks"]
    os.system('clear')
    for i in get_snacks:
        print(f"({i['ItemID']}) {i['ItemName']} - ${i['ItemPrice']}")
    print("\n(0) Back to main menu")
    print("\n\nPlease enter your choice: ")
    choice = int(input())
    if choice in [201, 202, 203, 204, 205]:
        choose_snacks.append(choice)
        print(f"You have selected {get_snacks[choice - 201]['ItemName']}")
    elif choice == 0:
        print("You will be redirected back to the main menu")
        interface(total_drink,choose_snacks)
    else:
        print("Please enter a valid choice")
        displaysnacks(choose_snacks, total_drink)
    os.system('clear')
    print("Would you like to add another item?")
    print("(1) Yes")
    print("(2) No")
    print("Please enter your choice: ")
    choice = int(input())
    if choice == 1:
        displaysnacks(choose_snacks, total_drink)
    elif choice == 2:
        interface(total_drink,choose_snacks)
    else:
        print("Please enter a valid choice!")
        displaysnacks(choose_snacks, total_drink)
    

def calculate_total(total_drink, total_snacks):
    total_price = 0
    
    # Retrieve the list of drinks and snacks
    drink_list = item.option[0]["Drinks"]
    snack_list = item.option[1]["Snacks"]
    
    # Add drinks prices to the total
    for drink_id in total_drink:
        for drink in drink_list:
            if drink["ItemID"] == drink_id:
                total_price += drink["ItemPrice"]
                break
    
    # Add snacks prices to the total
    for snack_id in total_snacks:
        for snack in snack_list:
            if snack["ItemID"] == snack_id:
                total_price += snack["ItemPrice"]
                break
    
    return(total_price)


interface()
