def show_choices():
    print("A. Right Triangle Pattern")
    print("B. Pyramid Pattern")
    print("C. Left Triangle Pattern")
    print("D. Numbers (Total, Average, Even Numbers)")

show_choices()

user_choice = input("Enter your choice (A, B, C, or D): ").upper()

if user_choice == "A":
    print("You selected A. Right Triangle Pattern:")
    rows = 8
    for i in range(1, rows + 1):
        print('*' * i)

elif user_choice == "B":
    print("You selected B. Pyramid Pattern:")
    rows = 5
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif user_choice == "C":
    print("You selected C. Left Triangle Pattern:")
    rows = 6
    for i in range(1, rows + 1):
        print('*' * i)

elif user_choice == "D":
    print("You selected D. Numbers Calculation:")
    numbers = range(1, 11)
    total = sum(numbers)
    average = total / len(numbers)
    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Total:", total)
    print("Average:", average)
    print("Even Numbers:", even_numbers)

else:
    print("Invalid choice!")b
