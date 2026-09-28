# base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person Details:")
        print("Name:", self.name)
        print("Age:", self.age)

# Inheritance and Encapsulation
class Employee(Person):
    def __init__(self, name, age, employee_id=None, salary=None):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter and Setter   
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

 # Method Overriding
    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

  # Destructor
    def __del__(self):
        print("Employee object deleted.")

# Manager inherits Employee
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department


    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)

# Developer inherits Employee
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("Developer Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:", self.programming_language)


person1 = None
employee1 = None
manager1 = None
developer1 = None

# Menu Driven Program
while True:
    print()
    print("--- Python OOP Project: Employee Management System ---")
    print()
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person1 = Person(name, age)

        print()
        print("Person created with name:", name, "and age:", age)

    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee1 = Employee(name, age, employee_id, salary)

        print()
        print("Employee created with name:", name, 
              "age:", age, 
              "ID:", employee_id, 
              "and salary:", salary)

    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager1 = Manager(name, age, employee_id, salary, department)

        print()
        print("Manager created with name:", name,
              "age:", age,
              "ID:", employee_id,
              "salary:", salary,
              "and department:", department)

    elif choice == "4":
        print()
        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        detail_choice = input("Enter your choice: ")

        if detail_choice == "1":
            if person1:
                person1.display()
            else:
                print("Person not created.")

        elif detail_choice == "2":
            if employee1:
                employee1.display()
            else:
                print("Employee not created.")

        elif detail_choice == "3":
            if manager1:
                manager1.display()
            else:
                print("Manager not created.")

        elif detail_choice == "4":
            if developer1:
                developer1.display()
            else:
                print("Developer not created.")

        else:
            print("Invalid choice.")

    elif choice == "5":
        print()
        print("Exiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")