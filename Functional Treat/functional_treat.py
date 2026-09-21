data = []
summary = 0

# input data - 1D and 2D array
def input_data():
    """Take 1D or 2D list input from user."""
    global data

    choice = input("Enter 1 for 1D array or 2 for 2D array: ")

    if choice == "1":
        values = input("Enter data for a 1D array (separated by spaces): ")
        data = list(map(int, values.split()))

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        data = []

        for i in range(rows):
            values = input("Enter row " + str(i + 1) + ": ")
            row = list(map(int, values.split()))
            data.append(row)

    else:
        print("Invalid choice.")
        return

    print("\nData has been stored successfully!")

# Bulit-in Functions 
def display_summary():
    """Display basic dataset information using built-in functions."""
    global summary

    if len(data) == 0:
        print("No data available.")
        return

    if type(data[0]) == list:
        values = []

        for row in data:
            for i in row:
                values.append(i)
    else:
        values = data

    summary = len(values)

    print("\nData Summary:")
    print("- Total elements:", len(values))
    print("- Minimum value:", min(values))
    print("- Maximum value:", max(values))
    print("- Sum of all values:", sum(values))
    print("- Average value:", round(sum(values) / len(values), 2))

# recursion- Factorial 
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

# Lambda and Filter Function
def filter_data():
    """Filter values using lambda and filter."""
    if len(data) == 0:
        print("No data available.")
        return

    if type(data[0]) == list:
        values = []

        for row in data:
            for i in row:
                values.append(i)
    else:
        values = data

    threshold = int(input("\nEnter a threshold value to filter out data above this value: "))

    result = list(filter(lambda x: x >= threshold, values))

    print("\nFiltered Data (values >= " + str(threshold) + "):")

    for i in result:
        print(i, end=" ")

# sorting using sort()
def sort_data():
    """Sort the dataset in ascending or descending order."""
    if len(data) == 0:
        print("No data available.")
        return

    if type(data[0]) == list:
        values = []

        for row in data:
            for i in row:
                values.append(i)
    else:
        values = data.copy()

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        values.sort()
        print("\nSorted Data in Ascending Order:")

    elif choice == "2":
        values.sort(reverse=True)
        print("\nSorted Data in Descending Order:")

    else:
        print("Invalid choice.")
        return

    for i in values:
        print(i, end=" ")

# Multiple Return Values
def dataset_statistics():
    """Return minimum, maximum, sum and average values."""
    if len(data) == 0:
        print("No data available.")
        return

    if type(data[0]) == list:
        values = []

        for row in data:
            for i in row:
                values.append(i)
    else:
        values = data

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total / len(values)

    return minimum, maximum, total, average

# *args
def show_args(*args):
    """Display multiple values using *args."""
    print("\nValues using *args:")

    for i in args:
        print(i, end=" ")

# **kwargs
def show_kwargs(**kwargs):
    """Display dataset information using **kwargs."""
    print("\n\nDataset information using **kwargs:")

    for key, value in kwargs.items():
        print(key + ":", value)

# Main Menu
def main():
    """Main menu of Data Analyzer and Transformer Program."""

    while True:
        print("\n\nmain menu")
        print("1.Input Data")
        print("2.Diaplay Data Summary (bulit-in functions)")
        print("3.Calculate Factorial (recursion)")
        print("4.Filter Data By Threshold (Lambda Function)")
        print("5.Sort Data")
        print("6.Display Dataset Statistics (return multiple values)")
        print("7. Exit Program")

        choice = input("\nPlease enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            display_summary()

        elif choice == "3":
            n = int(input("\nEnter a number to calculate its factorial: "))
            result = factorial(n)
            print("\nFactorial of", n, "is:", result)

        elif choice == "4":
            filter_data()

        elif choice == "5":
            sort_data()

        elif choice == "6":
            result = dataset_statistics()
            if result:
                minimum, maximum, total, average = result
                print("\nDataset Statistics:")
                print("_ minimum value:", minimum)
                print("_ maximum value:", maximum)
                print("_ sum of all values:", total)
                print("_ average value:", round(average, 2))

        elif choice == "7":
            print("Thank you sir !")
            break

        else:
           print("Wrong choice. Please try again.")


if __name__ == "__main__":
    main()
