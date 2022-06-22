from classes.menu import Menu, MenuItem
from classes.coffee_maker import CoffeeMaker
from classes.money_machine import MoneyMachine


def order_drink():
    menu = Menu()

    drink = input(f'What would you like? ({menu.get_items()}): ')
    if menu.find_drink(drink) is not None:
        print(f'{drink} is being dispensed')
    else:
        order_drink()


if __name__ == '__main__':
    order_drink()

