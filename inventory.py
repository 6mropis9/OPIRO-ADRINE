inventory = {}

def display_menu():
    print("\nSimple Inventory System")
    print("1. Add item")
    print("2. View inventory")
    print("3. Update quantity")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ")
        if item in inventory:
            print(f"{item} already exists.")
        else:
            quantity = input("Enter quantity: ")
            if quantity.isdigit():
                inventory[item] = int(quantity)
                print(f"{item} added.")
            else:
                print("Invalid quantity.")

    elif choice == '2':
        if inventory:
            print("\nInventory:")
            for item, qty in inventory.items():
                print(f"{item}: {qty}")
        else:
            print("Inventory is empty.")

    elif choice == '3':
        item = input("Enter item name to update: ")
        if item in inventory:
            quantity = input("Enter new quantity: ")
            if quantity.isdigit():
                inventory[item] = int(quantity)
                print(f"{item} updated.")
            else:
                print("Invalid quantity.")
        else:
            print(f"{item} not found.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
