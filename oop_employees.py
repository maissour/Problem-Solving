'''
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department 
and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
which is the number of hours worked by the employee. If the number of hours worked is 
more than 50, the method computes overtime and adds it to the salary. 
Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
'''

class Employee :

    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_dept):

        self.emp_department = new_dept
        return self.emp_department

    def print_employee_details(self, EmpName):
        if self.emp_name == EmpName :
            print(f"{self.emp_name} is an employee in {self.emp_department} department and has {self.emp_salary} $ salary")

    def calculate_emp_salary(self, EmpName, hours_worked):
        if self.emp_name == EmpName :
            if int(hours_worked) <= 50 :
                print(f"the salary of {self.emp_name} for this month is {self.emp_salary}")
            
            else :
                overtime = int(hours_worked) - 50
                Overtime_amount = (overtime * (self.emp_salary / 50))
                salary = self.emp_salary + Overtime_amount
                print(f"the salary of {self.emp_name} for this month is {salary}")

print("#"*10)
emp1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
print(emp1.assign_department("IT"))
print("#"*10)
emp1.print_employee_details("ADAMS")
print("#"*10)
emp1.calculate_emp_salary("ADAMS",60)
print("#"*10)
