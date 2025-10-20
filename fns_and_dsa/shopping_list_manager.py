class ItemNotFoundError(Exception):
    pass

shopping_list = []

def add_item(list_item, shopping_list):
    if list_item not in shopping_list:
        shopping_list.append(list_item)
        print(f"{list_item} has been added to the shopping list.")
    else:
        raise ValueError(f"{list_item} is already in the shopping list.")
    

def remove_item(list_item, shopping_list):
    if list_item in shopping_list:
        shopping_list.remove(list_item)
    else:
        raise ItemNotFoundError(f"{list_item} is not found in the shopping list.")

def display_list():
    print("Shopping List:")
    count = 1
    for item in shopping_list:
        print(f"{count}. {item}")
        count += 1


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # ADD
            item_name = input("Enter the name of item to add: ")
            add_item(item_name, shopping_list)
            print(f"{item_name} has been added to the Shopping List.")
            pass
        elif choice == '2':
            # Remove
            item_name = input("Enter the name of item to remove from Shopping List: ")
            try:
                remove_item(item_name, shopping_list)
            except ItemNotFoundError as e:
                print(e)

            pass
        elif choice == '3':
            # Display
            display_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    