pattern_size = int(input("Enter the size of the pattern: "))
row_count = 0

while row_count < pattern_size:
    for i in range(pattern_size):
        print("*", end="")
    print()
    row_count += 1
