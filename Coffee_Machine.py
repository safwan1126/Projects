MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check(coin):
    while True:
        ans = input(f'Insert {coin}: ')
        if ans.isdigit():
            if int(ans) > 100:
                print('You can only insert 100 coins boss')
            else:
                break
        else:
            print('That\'s not a whole number of coins')
    return int(ans)


def insert():
    cents = check('cents')
    nickels = check('nickels')
    dimes = check('dimes')
    quarters = check('quarters')
    total = 0.01 * cents + 0.05 * nickels + 0.1 * dimes + 0.25 * quarters
    return total


def enough_resources(option):
    if 'water' not in MENU[option]['ingredients']:
        pass
    elif MENU[option]['ingredients']['water'] < resources["water"]:
        resources["water"] -= MENU[option]['ingredients']['water']
    else:
        return False
    if 'coffee' not in MENU[option]['ingredients']:
        pass
    elif MENU[option]['ingredients']['coffee'] < resources["coffee"]:
        resources["coffee"] -= MENU[option]['ingredients']['coffee']
    else:
        return False
    if 'milk' not in MENU[option]['ingredients']:
        pass
    elif MENU[option]['ingredients']['milk'] < resources["milk"]:
        resources["milk"] -= MENU[option]['ingredients']['milk']
    else:
        return False
    return True


print("Welcome to Safwan's coffee machine ")

while True:
    while True:
        choice = input('What coffee would you like? Choose either espresso'
                       ', latte or cappuccino: ').lower().replace(' ', '')
        if choice in MENU:
            break
        elif choice == 'report':
            print(f"Water : {resources['water']} ml")
            print(f"Milk : {resources['milk']} ml")
            print(f"Coffee : {resources['coffee']} g")
            print(f'Money : ${money}')
        else:
            print("That's not a valid option")
    money = insert()
    if enough_resources(choice) and money > MENU[choice]['cost']:
        print(f'Here is your {choice}')
    elif enough_resources(choice):
        print('Not enough money')
    else:
        print('Not enough resources')
