from coffee_data import menu, resources
# set initial profit
profit = 0


def process_coins():
    """This will take all the required coins and return total coins"""
    print("Please insert coins.")
    total_coins = int(input("How many quarters?: ")) * .25
    total_coins += int(input("How many dimes?: ")) * .10
    total_coins += int(input("How many nickles?: ")) * .05
    total_coins += int(input("How many pennies?: ")) * .01
    return total_coins


def is_resource_sufficient(order_resource):
    """It returns true if resource is available and return false if resource is not available"""
    for item in resources:
        if order_resource[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def is_transaction_success(user_cost, drink_cost):
    if user_cost >= drink_cost:
        change = round(user_cost - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}. Enjoy 🍵🍵")


is_end = False
# ask  user
while not is_end:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_end = True
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        is_available = is_resource_sufficient(drink['ingredients'])
        if is_available:
            user_coins = process_coins()
            if is_transaction_success(user_coins, drink["cost"]):
                make_coffee(choice, drink['ingredients'])
