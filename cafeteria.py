from prettytable import PrettyTable
import json


with open("snacks.json", "r") as json_file:
    existing_snacks = json.load(json_file)


table = PrettyTable(["ID", "Name", "Price", "Availability"])
for item in existing_snacks:
    table.add_row([item["id"], item["name"], item["price"], item["availability"]])

print("--------------------------------------------------------------")
print("+-+-+-+-+-+-+-+-+-+-WELCOME TO MUMBAI MUNCHIES+-+-+-+-+-+-+-+-")
print("--------------------------------------------------------------")
print("")
# print("————————————————————————————")


while True:
    print("1.  Menu List ")
    print("2.  Add A Snack")
    print("3.  Delete A Snack")
    print("4.  Update Availability of a Snack")
    print("5.  Update the Price of a Snack")
    print("6.  Record a Sale")
    print("")

    user_input = input("Select Your Option: ")

    if user_input == "2":
        while True:
            snack_id = input("Enter Snack ID: ")
            if snack_id.isdigit():
                snack_id = int(snack_id)
                id_present = any(int(item["id"]) == snack_id for item in existing_snacks)
                if id_present:
                    print(f"ID {snack_id} is already present in the list.")
                else:
                    break
            else:
                print("Invalid input. Please enter a valid snack ID (numeric).")

        snack_name = input("Enter Snack Name: ")
        
        while True:
            snack_price = input("Enter Snack Price: ")
            if snack_price.isdigit():
                snack_price = int(snack_price)
                break
            else:
                print("Invalid input. Please enter a valid number for the snack price.")

        snack_availability = input("Enter Snack Availability: ")

        new_snack = {
            "id": snack_id,
            "name": snack_name,
            "price": snack_price,
            "availability": snack_availability
        }

        existing_snacks.append(new_snack)

        with open("snacks.json", "w") as json_file:
            json.dump(existing_snacks, json_file)
        
        table.add_row([new_snack["id"], new_snack["name"], int(new_snack["price"]), new_snack["availability"]])
        print("\n" + str(table))

    if user_input == "3":
        delete_id = input("Enter ID of Snack to Delete: ")
        for item in existing_snacks:
            if item["id"] == delete_id:
                existing_snacks.remove(item)
                break

        with open("snacks.json", "w") as json_file:
            json.dump(existing_snacks, json_file)
            table = PrettyTable(["ID", "Name", "Price", "Availability"])
            for item in existing_snacks:
                table.add_row([item["id"], item["name"], item["price"], item["availability"]])
            print("\n" + str(table))

    if user_input == "4":
        availability_update = input("Enter name of Snack to update Availability: ")
        for item in existing_snacks:
            if item["name"] == availability_update:
                item["availability"] = "no" if item["availability"] == "yes" else "yes"
                break

        with open("snacks.json", "w") as json_file:
            json.dump(existing_snacks, json_file)
            table = PrettyTable(["ID", "Name", "Price", "Availability"])
            for item in existing_snacks:
                table.add_row([item["id"], item["name"], item["price"], item["availability"]])
            print("\n" + str(table))

    if user_input == "5":
        price_update_by_name = input("Enter name of Snack to update its Price: ")
        for item in existing_snacks:
            if item["name"] == price_update_by_name:
                updated_price =input(f"Enter the updated price for {item['name']}: ")
                item["price"] = updated_price
                print("")
                print("Price Updated Successfully")
                break

        with open("snacks.json", "w") as json_file:
            json.dump(existing_snacks, json_file)
            table = PrettyTable(["ID", "Name", "Price", "Availability"])
            for item in existing_snacks:
                table.add_row([item["id"], item["name"], item["price"], item["availability"]])
            print("\n" + str(table))

    if user_input == "1":
        print("\n" + str(table) + "\n")
    print("")
    decision = input("Do you want to close the Canteen (yes/no): ")
    if decision.lower() == "yes":
        break
    else:
        print("")

