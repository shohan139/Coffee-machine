# Coffee-machine

## Fixes

1. expand this documentation by sharing with the user how to run the app, which options he might have, and so on **OK**
1. what do you mean by `type "report" at any moment`? It's not clear **OK**
1. when I need to insert coins, if I insert a not numeric value I should stay there **OK**
1. please switch the menu options by using the numbers. Try to think of real life. When you go to a coffee machine you don't have to type in the name of the desired beverage, a simple number is enough **OK**
1. when you type the wrong beverages (wrong number after the changes mentioned above) you should stay in the menu, not exit the application **OK**
1. add the exit option as the last one in the menu **OK**
1. keep decreasing the amount of the due money as long as we insert coins (updated this one too)
1. don't ask for dimes, nickels, and pennies if we've already inserted enough money. You force the user to type three useless zeros (updated this one too)
1. add a check on the number of coins inserted by the user. Otherwise, the user can insert an endless number of coins (updated by asking if he wishes to continue or stop there)
2. if you do a second operation it won't manage the remainder correctly (such as I take another cappuccino)
3. the insert money function is not clear: it only asks me to `Enter your money:`. As mentioned above, you should keep asking for money and decrease the amount due. (updated this one. If you have enough money and you want to purchase again, it will not ask for any money)
4. When you ask to prompt the number for the beverage you can omit the sentence `Options (latte/espresso/cappuccino)` since it's already defined in the user menu (updated this one)

<h1>Coffee Machine</h1>
<h3>Overview</h3>
<p>
This project implements a simple interactive coffee machine simulation. Users can select various coffee options, make payments, and receive their chosen beverages. The project is divided into modular files, each handling specific functionalities.
</p>


<h4>Files</h4>
1. main.py
Description: The main script that orchestrates the coffee machine simulation.
Responsibilities:
User interface and menu interaction.
Integration of Menu, MoneyMachine, and CoffeeMaker functionalities.
2. menu.py
Description: Defines the menu and menu item classes for different coffee options.
Responsibilities:
Menu item creation and initialization.
Retrieving available menu items and finding a specific drink.
3. money_machine.py
Description: Manages the financial aspects of the coffee machine, including payment and change calculation.
Responsibilities:
Handling user input for money.
Processing payments and making change.
Keeping track of profits.
4. coffee_maker.py
Description: Simulates the coffee-making process.
Responsibilities:
Deducting required ingredients from available resources.
Displaying a message for the user when the coffee is ready.
How to Run the Coffee Machine Project
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Run the Coffee Machine:

bash
Copy code
python main.py
Interact with the Menu:

Follow the on-screen instructions to choose a coffee option.
Enter the corresponding number for your desired coffee.
Make Payments:

Enter the required amount when prompted.
Repeat or Exit:

After making a purchase, choose to make another purchase or exit the program.
View Profits:

Check the current profits by selecting the 'Report' option in the main menu.
Dependencies
Python 3.x
Notes
ANSI escape codes are used for colored output. Make sure your terminal supports ANSI escape codes for the best visual experience.
