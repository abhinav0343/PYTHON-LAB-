class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return self.salary - other.salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

def main():
    employees = []

    while True:
        print("\nOptions:")
        print("1. Add Employee")
        print("2. Combine Employees")
        print("3. Compare Employees")
        print("4. Display Employees")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))
            employees.append(Employee(name, salary))
        elif choice == 2:
            if len(employees) < 2:
                print("Need at least two employees to combine.")
            else:
                print("Select employees to combine:")
                for i, emp in enumerate(employees):
                    print(f"{i+1}. {emp}")
                idx1 = int(input("Enter first employee number: ")) - 1
                idx2 = int(input("Enter second employee number: ")) - 1
                combined_employee = employees[idx1] + employees[idx2]
                print(f"Combined Employee: {combined_employee}")
        elif choice == 3:
            if len(employees) < 2:
                print("Need at least two employees to compare.")
            else:
                print("Select employees to compare:")
                for i, emp in enumerate(employees):
                    print(f"{i+1}. {emp}")
                idx1 = int(input("Enter first employee number: ")) - 1
                idx2 = int(input("Enter second employee number: ")) - 1
                difference = employees[idx1] - employees[idx2]
                print(f"Salary Difference: {difference}")
        elif choice == 4:
            if not employees:
                print("No employees to display.")
            else:
                for emp in employees:
                    print(emp)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
