number = int(input("Enter a number to see its multiplication table: "))

for iterator in range(1, 11):
    print(f"{number} * {iterator} =", number * iterator)