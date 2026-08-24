print("===== Personal Data Collector =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
favourite_number = int(input("Enter your favourite number: "))

print("\n===== Your Information =====")

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Favourite Number:", favourite_number)

# Birth year
birth_year = 2026 - age
print("Approximate Birth Year:", birth_year)

# Arithmetic operators
print("Age + Favourite Number:", age + favourite_number)
print("Age - Favourite Number:", age - favourite_number)

# Type casting
height_int = int(height)
print("Height as float:", height)
print("Height as integer:", height_int)

# type() and id()
print("\n===== Data Type and Memory Information =====")

print("Name - Type:", type(name), "ID:", id(name))
print("Age - Type:", type(age), "ID:", id(age))
print("Height - Type:", type(height), "ID:", id(height))
print("Favourite Number - Type:", type(favourite_number), "ID:", id(favourite_number))
print("\nThank you for using Personal Data Collector!")
