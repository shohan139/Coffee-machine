# Coffee-machine

## Fixes

1. expand this documentation by sharing with the user how to run the app, which options he might have, and so on **OK**
1. what do you mean by `type "report" at any moment`? It's not clear **OK**
1. when I need to insert coins, if I insert a not numeric value I should stay there **OK**
1. please switch the menu options by using the numbers. Try to think of real life. When you go to a coffee machine you don't have to type in the name of the desired beverage, a simple number is enough **OK**
1. when you type the wrong beverages (wrong number after the changes mentioned above) you should stay in the menu, not exit the application **OK**
1. add the exit option as the last one in the menu **OK**
1. keep decreasing the amount of the due money as long as we insert coins
1. don't ask for dimes, nickels, and pennies if we've already inserted enough money. You force the user to type three useless zeros
1. add a check on the number of coins inserted by the user. Otherwise, the user can insert an endless number of coins
2. if you do a second operation it won't manage the remainder correctly (such as I take another cappuccino)
3. the insert money function is not clear: it only asks me to `Enter your money:`. As mentioned above, you should keep asking for money and decrease the amount due.
4. When you ask to prompt the number for the beverage you can omit the sentence `Options (latte/espresso/cappuccino)` since it's already defined in the user menu

An OOP-based coffee machine simulation project. It allows users to select different types of coffee, check available resources, make purchases, and handle the financial aspect of the transactions.
