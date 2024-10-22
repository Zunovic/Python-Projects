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


def enough_materials(order_materials):
    # Gibt True zurück, wenn genug Material vorhanden ist. False, wenn nicht.
    for i in order_materials:
        if order_materials[i] >= resources[i]:
            print(f"Es ist nicht genug {i} vorhanden.")
            return False
    return True


def check_coins():
    # Gibt den eingeworfenen Geldbetrag aus.
    print("Bitte Geld einwerfen:")
    total = int(input("Wie viele 2    € Münzen: ") or 0) * 2
    total += int(input("Wie viele 1    € Münzen: ") or 0)
    total += int(input("Wie viele 0.5  € Münzen: ") or 0) * 0.5
    total += int(input("Wie viele 0.2  € Münzen: ") or 0) * 0.2
    total += int(input("Wie viele 0.1  € Münzen: ") or 0) * 0.1
    return total


def transaction(money_recv, drink_cost):
    # Gibt True zurück, wenn die Zahlung funktioniert und False, wenn nicht.
    if money_recv >= drink_cost:
        change = round(money_recv - drink_cost, 2)
        print(f"Rückgeld beträgt: {change} €")
        global money_inside
        money_inside += drink_cost
        return True
    else:
        change = round(money_recv - drink_cost, 2)
        print(f"Die Zahlung hat leider nicht funktioniert! {change}€ fehlen!")
        return False


def make_coffee(drink_name, order_materials):
    # Zieht die Zutaten ab und ersetzt die Zahl durch die neue Zahl
    for i in order_materials:
        resources[i] -= order_materials[i]
    print(f"Hier ist der {drink_name}")


money_inside = 0
machine_on = True

while machine_on:
    choice = input("Was möchtest du trinken? Espresso, Latte, Cappuccino : ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Wasser: {resources['water']} ml")
        print(f"Milch: {resources['milk']} ml")
        print(f"Kaffee: {resources['coffee']} g")
        print(f"Geld: {money_inside} €")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if enough_materials(drink["ingredients"]):
            payment = check_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Falsche Eingabe! Bitte wähle ein Getränk aus.")
