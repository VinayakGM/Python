from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
# menuitem=MenuItem()
coffemaker=CoffeeMaker()
moneymachine=MoneyMachine()

is_on=True

while is_on:
    options=menu.get_items()
    # print(options)
    user_input=input("what you would like to have ?  ")
    if user_input=="off":
        is_on=False
    elif user_input=="report":
        coffemaker.report()
        moneymachine.report()
    else:
        drink=menu.find_drink(user_input)
        # print(drink)
        if coffemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffemaker.make_coffee()
