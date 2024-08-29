"""
User inputs who is on the date with them
User inputs their budget for the date
Print the restaurant menu (your group created this!) 
User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
Script tells the user how much money they have left after each order.
At the end of the date user must agree to pay the bill and then their final budget is shown to them.
Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision
"""

def get_date_name():
    # prompt user to input the date name
    dateName = input("Who are you going the date with? --> ")
    return dateName

def get_user_budget():
    # promt user to share their budget for the date.
    dateName = get_date_name()
    userBudget = float(input(f"Awesome! What's your budget to take {dateName} on a date? --> "))
    return userBudget

def display_menu():
# group 4 menu
    kuraCafeMenu={
    "Croissant":{"Price":"1.50","Ingredients":["flour","butter","eggs"]},
    "BaconEgg&Cheese":{"Price":"3.00","Ingredients":["bagel","cheese","eggs","bacon"]},
    "Cheesecake":{"Price":"1.00","Ingredients":["crust","cream cheese","eggs","blueberries"]},
    "Coffee":{"Price":"1.00","Ingredients":["colombian coffee beans","water"]}
    }
    return kuraCafeMenu

def get_user_order():
    userOrder = input("What would you like to order? (Enter 'done' to finish): ")
    return userOrder

def start_date():
    dateName = get_date_name()
    userBudget = get_user_budget()

    # initialize remaining budget
    remainingBudget = userBudget

    # loop through user orders
    while True:
    # prompt user to input their order
        userOrder = get_user_order()
        # check if user wants to finish ordering
        if userOrder.lower() == "done":
            break

        kuraCafeMenu = display_menu()
        print("!!Kura Cafe Menu!!")
        print("======================\n")
        print(f"{kuraCafeMenu}")
        print("-------------------------------------------------------------------\n")
        print("Please get ready to order now....")

        # check if user's order is in the menu
        if userOrder not in kuraCafeMenu:
            print("Sorry, that item is not on the menu.")
            continue

        # get item price
        
        itemPrice = float(kuraCafeMenu[userOrder]["Price"])

        display_price = input(f"Do you want to know the price for {userOrder}? (yes/no)")
        if display_price == "yes":
            print(f"{userOrder} costs ${itemPrice}")

        # ask user if they want to know the ingrdients
        ingredients = input(f"Do you want to know the ingrdients for {userOrder}? (yes/no)")
        if ingredients == "yes":
            print(f"Ingredients for {userOrder} are {kuraCafeMenu[userOrder]['Ingredients']}")

        # check if user can afford the item
        if itemPrice > remainingBudget:
            print("You don't have enough money for that.")
            continue

        # update remaining budget
        remainingBudget -= itemPrice

        # print remaining budget
        print(f"You have ${remainingBudget:.2f} left.")

        # prompt user to pay the bill
        payment = input("Are you ready to pay the bill? (yes/no): ")
        if payment.lower() == "yes":
            print(f"Your final bill is ${userBudget - remainingBudget:.2f}.")

        # determine if user will get a second date based on remaining budget
            if remainingBudget >= 0:
                print(f"Great job budgeting! You are very lucky {dateName}, you both should come here for your second date!")
            else:
                print("Oh no!! you might want to work on your budgeting skills for the next date. Contact Laxmi, our Budget Expert!! ")
        else:
            print("Payment cancelled.")

# call the start date function
start_date()