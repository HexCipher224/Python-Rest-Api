import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n====== Inventory Management CLI ======")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Product by Barcode")
    print("6. Exit")


while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        response = requests.get(f"{BASE_URL}/items")
        print(response.json())

    elif choice == "2":
        name = input("Item name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        data = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        response = requests.post(f"{BASE_URL}/items", json=data)
        print(response.json())

    elif choice == "3":
        item_id = input("Item ID: ")

        data = {}

        name = input("New name (leave blank to keep): ")
        if name:
            data["name"] = name

        quantity = input("New quantity (leave blank to keep): ")
        if quantity:
            data["quantity"] = int(quantity)

        price = input("New price (leave blank to keep): ")
        if price:
            data["price"] = float(price)

        response = requests.patch(f"{BASE_URL}/items/{item_id}", json=data)
        print(response.json())

    elif choice == "4":
        item_id = input("Item ID: ")

        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        print(response.json())

    elif choice == "5":
        barcode = input("Enter barcode: ")

        response = requests.get(f"{BASE_URL}/search/{barcode}")
        print(response.json())

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")