items = {
    # Chips - 4 AED
    1: ("Cheetoes", 4),2: ("Doritos", 4), 3: ("Lays", 4),
    4: ("Kurkure", 4), 5: ("Oman Chips", 4),6: ("Pringles", 4),
    7: ("Bugles", 4), 8: ("Lays Max", 4), 9: ("Mr Krips", 4),
    10: ("Takis", 4),

    # Candy - 2 AED
    11: ("M&Ms", 2),12: ("Gumballs", 2),13: ("Skittles", 2),
    14: ("Hello Panda", 2),15: ("Pop Rocks", 2),16: ("Sour Candy", 2),
    17: ("Bubble Gum", 2),18: ("Lollipop", 2),19: ("Chocolate Coins", 2),
    20: ("Jelly Beans", 2),

    # Drinks - 5 AED
    21: ("Water", 5),22: ("Coca Cola", 5),23: ("Pepsi", 5),
    24: ("Sprite", 5),25: ("Fanta", 5),26: ("Red Bull", 5),
    27: ("Mountain Dew", 5),28: ("Ice Tea", 5),29: ("Orange Juice", 5),
    30: ("Energy Drink", 5),31: ("Oreo", 3),32: ("Digestive Biscuits", 3),
    33: ("Marie Biscuits", 3),34: ("Chocolate Wafer", 3),
    35: ("Cheese Crackers", 3),

    # Hot Drinks - 6 AED
    36: ("Coffee", 6),37: ("Tea", 6),38: ("Hot Chocolate", 6),
    39: ("Cappuccino", 6),40: ("Latte", 6),
    }

def show_menu():
    print("\n--- UNIVERSITY VENDING MACHINE ---")
    for code, (name, price) in items.items():
        print(f"{code} - {name} : {price} AED")
    print("---------------------------------")

def get_money():
    while True:
        try:
            money = float(input("Insert money (AED): "))
            if money > 0:
                return money
            else:
                print("Please insert a valid amount.")
        except ValueError:
            print("Numbers only.")

def get_code():
    try:
        return int(input("Enter item code: "))
    except ValueError:
        return None
    
def main():
    print("Welcome to the University Vending Machine")
    balance = get_money()

    while True:
        show_menu()
        code = get_code()

        if code in items:
            name, price = items[code]
            if balance >= price:
                balance -= price
                print(f"\nDispensing: {name}")
                print(f"Remaining balance: {balance:.2f} AED")
            else:
                print("Insufficient funds for this item.")
        else:
            print("Invalid item code.")

        again = input("\nDo you want to buy another item? (yes/no): ").lower()
        if again != 'yes':
            print(f"\nTransaction ended. Remaining change: {balance:.2f} AED")
            break

# Run the vending machine
main()