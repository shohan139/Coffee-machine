from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----' 
    
          ------ MENU ------ 
          1. Espresso ($1.50)
          2. Latte ($2.50)
          3. Cappuccino ($3.00)
          4. Exit
          ------------------
    
          \033[m
        ''')



menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    welcome()
    options = menu.get_items()
    flag = 0
    try:
        user_choice = int(input(f"What would you like?\nOptions ({options}): "))
    except:
        print("Wrong input! Please enter number shown in the menu only!")
        flag = 1
    
    if flag == 1:
        continue
    elif user_choice<=0 or user_choice>4:
        print("Please enter 1 to 4 only!")
    else:
        if user_choice == 4:
            print("\033[31m<<THE END>>\033[m")
            break
        else:
            user_choice = menu.set_items(user_choice)
            beverage = menu.find_drink(user_choice) # Encapsulates the result
            if beverage == 0:
                break
            sufficient_resources = coffee_maker.is_resource_sufficient(beverage)  # TrueFalse result
            sufficient_money = money_machine.make_payment(beverage.cost)  # Encapsulates
            if sufficient_resources and sufficient_money:
                print("Thank you! Allow us to make your beverage now..")
                coffee_maker.make_coffee(beverage)
                sleep(5)
