class ItemNotFoundError(Exception):
    pass

shopping_list = []

def add_item(list_item, shopping_list):
    if list_item not in shopping_list:
        shopping_list.append(list_item)
    

def remove_item(list_item, shopping_list):
    if list_item in shopping_list:
        shopping_list.remove(list_item)
    else:
        raise ItemNotFoundError(f"{list_item} is not found in the shopping list.")

def view_list(shopping_list):
    print("Shopping List:")
    count = 1
    for item in shopping_list:
        print(f"{count}. {item}")
        count += 1
    