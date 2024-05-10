import os
import item

def interface(*args):
    choose_drink = []
    os.system('clear')
    total_drink = args[0] if args else []
    total_price = 0
    print("""
        ------------------------------------
          Welcome to Tsuna's Vending Machine!
        ------------------------------------
        """)
    print("Please choose a category:")
    print("(1) Drinks")
    print("(2) Payment")
    print("(0) Exit")
    print("\nPlease enter your choice: ")
    choice = int(input())
    if choice == 1:
        displaydrinks(choose_drink)
    elif choice == 2:
        total_price = calculate_total(total_drink)
        print(f"\nTotal price: ${total_price}")
        print("\nPlease enter the amount you want to pay: $")
        payment = float(input())
        if payment < total_price:
            print("Insufficient amount! Please enter a higher amount.")
            interface(*args)
        else:
            change = payment - total_price
            print(f"Thank you for your payment of ${payment:.2f}. Your change is ${change:.2f}.")
            print("\nThank you for shopping with us!")
            print("------------------------------------")
            print("\nWould you like a receipt?\n")
            print("(1) Yes")
            print("(2) No")
            print("\nPlease enter your choice: ")
            sub_choice = int(input())
            if sub_choice == 1:
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
                print(f"\nTotal price: ${total_price}")
                print(f"Payment: ${payment:.2f}")
                print(f"Change: ${change:.2f}")
                print("\nThank you for shopping and purchasing items from Tsuna's Vending Machine! Have a nice Day!")
            elif sub_choice == 2:
                print("You will be redirected back to the main menu")  
                interface()
            else:
                print("Please enter a valid choice")
                interface()
    elif choice == 0:
        exit()
    else:
        print("Please enter a valid choice")
        interface(*args)


def displaydrinks(choose_drink):
    get_drinks = item.option[0]["Drinks"]
    os.system('clear')
    print("Please choose a drink:")
    for i in get_drinks:
        print(f"({i['ItemID']}) {i['ItemName']} - ${i['ItemPrice']}")
    print("\n\nPlease enter your choice: ")
    choice = int(input())
    if choice in [111, 112, 113, 114, 115]:
        choose_drink.append(choice)
        print(f"You have selected {get_drinks[choice - 111]['ItemName']}")
        os.system('clear')
        print("Would you like to add another item?")
        print("(1) Yes")
        print("(2) No")
        print("Please enter your choice: ")
        add_another = int(input())
        if add_another == 1:
            displaydrinks(choose_drink)  # Loop back for more selections
        elif add_another == 2:
            interface(choose_drink)  # Proceed to payment or exit
        else:
            print("Please enter a valid choice")
            interface(choose_drink)  # Return to main menu if choice is invalid
    else:
        print("Please enter a valid choice")
        displaydrinks(choose_drink)


def calculate_total(total_drink):
    total_price = 0
    
    # Retrieve the list of drinks 
    drink_list = item.option[0]["Drinks"]
    
    # Add drinks prices to the total
    for drink_id in total_drink:
        for drink in drink_list:
            if drink["ItemID"] == drink_id:
                total_price += drink["ItemPrice"]
                break
    
    return(total_price)


interface()
