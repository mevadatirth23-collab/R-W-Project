# Simple Employee Management System using OOP
class Employee:
    def __init__(self, emp_id=None, name=None, age=None, salary=0.0):
        self.__emp_id = emp_id   # private
        self.__salary = salary
        self.name = name
        self.age = age
    # getter and setter for salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
    # getter and setter for emp_id
    def get_emp_id(self):
        return self.__emp_id
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id
    def display(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.__emp_id}, Salary: {self.__salary}"
    def __del__(self):
        print("Employee deleted:", self.name)
    # dunder methods
    def __str__(self):
        return f"{self.name} ({self.__emp_id})"
    def __eq__(self, other):
        return self.__salary == other.__salary
    def __lt__(self, other):
        return self.__salary < other.__salary
    def __gt__(self, other):
        return self.__salary > other.__salary

class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, dept):
        super().__init__(emp_id, name, age, salary)
        self.dept = dept
    def display(self):
        return super().display() + f", Dept: {self.dept}"

class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, lang):
        super().__init__(emp_id, name, age, salary)
        self.lang = lang
    def display(self):
        return super().display() + f", Lang: {self.lang}"

def main():
    employees = {}
    while True:
        print("\n--- Employee Management System ---")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Compare Salaries")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            print("Person created:", name, "Age:", age)
        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter ID: ")
            salary = float(input("Enter Salary: "))
            e = Employee(emp_id, name, age, salary)
            employees[emp_id] = e
            print("Employee created:", e.display())

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            m = Manager(emp_id, name, age, salary, dept)
            employees[emp_id] = m
            print("Manager created:", m.display())

        elif choice == "4":
            emp_id = input("Enter Employee ID to show: ")
            if emp_id in employees:
                print(employees[emp_id].display())
            else:
                print("Not found")

        elif choice == "5":
            id1 = input("Enter first ID: ")
            id2 = input("Enter second ID: ")
            if id1 in employees and id2 in employees:
                if employees[id1] > employees[id2]:
                    print(employees[id1].name, "has higher salary")
                elif employees[id1] < employees[id2]:
                    print(employees[id1].name, "has lower salary")
                else:
                    print("Both have same salary")
            else:
                print("ID not found")

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()