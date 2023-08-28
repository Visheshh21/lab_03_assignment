class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees
    
    def print_table(self):
        print("Employee ID\tName\tAge\tSalary")
        print("-------------------------------------")
        for emp in self.employees:
            print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")
    
    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)
        self.print_table()
    
    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)
        self.print_table()
    
    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)
        self.print_table()

# Create employee objects
employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

employee_table = EmployeeTable(employees)

print("Choose sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")

choice = int(input())

if choice == 1:
    employee_table.sort_by_age()
elif choice == 2:
    employee_table.sort_by_name()
elif choice == 3:
    employee_table.sort_by_salary()
else:
    print("Invalid choice")