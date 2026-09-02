print("===== welcome to the Pattern Generator and Number Analyzer =====")

# Display the menu options to the user
print("\nSelect an option:")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

#generate a pattern based on user input
if choice == 1:
    rows = int(input("Enter the number of rows for the pattern: "))
    for i in range(1, rows + 1):
        for j in range(i):
            print("* ", end="")
        print()
    print("Generate a Pattern selected")

#analyze numbers in a given range 
elif choice == 2:
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    total = 0

    print("\nNumbers in the range:")

    for number in range(start, end + 1):
        if number % 2 == 0:
            print(f"Number {number} is Even")
        else:
            print(f"Number {number} is Odd")

        total += number

    print("Sum of all numbers:", total)

   #exit the program 
elif choice == 3:
    print("Thank you sir !")

else:
    print("Wrong choice. Please try again.")