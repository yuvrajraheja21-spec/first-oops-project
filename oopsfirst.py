class Employee:

	num_of_employees = 0
	raise_amount = (1.04 , 1.05)

	def __init__(self, name, age, pay):
		self.name = name
		self.age = age
		Employee.num_of_employees += 1
		self.pay = pay
		self.email = f"{name.lower().replace(' ', '.')}.{age}@company.com"

	def fullname(self):
		return f"{self.name} {self.age}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount[1])  # Apply raise based on age group

print(Employee.num_of_employees)  # Output: 0
employee_1 = Employee('John Doe', 30, 50000)
employee_2 = Employee('Jane Smith', 25, 60000)

print(employee_1.email)  # Output: john.doe.30@company.com
print(employee_1.fullname())  # Output: John Doe 30
print(employee_1.pay)  # Output: 50000
employee_1.apply_raise()
print(employee_1.pay)  # Output: 52000
print(employee_2.email)  # Output: jane.smith.25@company.com
print(employee_2.fullname())  # Output: Jane Smith 25

print(employee_2.pay)  # Output: 60000

employee_2.apply_raise()  # Apply raise for employee_2
print(employee_2.pay)  # Output: 63000
print(Employee.raise_amount)  # Output: (1.04, 1.05)
print(Employee.__dict__)  
# Output: {'__module__': '__main__', 'raise_amount': (1.04, 1.05),
#  '__init__': <function Employee.__init__ at 0x7f8c8c3e4d30>, 
# 'fullname': <function Employee.fullname at 0x7f8c8c3e4dc0>, 
# 'apply_raise': <function Employee.apply_raise at 0x7f8c8c3e4e50>, 
# '__dict__': <attribute '__dict__' of 'Employee' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Employee' objects>, 
# '__doc__': None}
print(Employee.num_of_employees)  # Output: 2
class developer(Employee):
	def __init__(self, name, age, pay, employees=None):
		super().__init__(name, age, pay)
		self.employees = [] if employees is None else list(employees)

	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)

	def add_emp(self, emp):
		self.add_employee(emp)

	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def remove_emp(self, emp):
		self.remove_employee(emp)

	def print_employees(self):
		for emp in self.employees:
			print('-->', emp.fullname())

	def print_emp(self):
		self.print_employees()


dev_1 = developer('kush', 28, 70000)
dev_1.add_emp(employee_2)
print(dev_1.email)


class manager(Employee):
	def __init__(self, name, age, pay, employees=None):
		super().__init__(name, age, pay)
		self.employees = [] if employees is None else list(employees)

	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)

	def add_emp(self, emp):
		self.add_employee(emp)

	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def remove_emp(self, emp):
		self.remove_employee(emp)

	def print_employees(self):
		for emp in self.employees:
			print('-->', emp.fullname())

	def print_emp(self):
		self.print_employees()


mgr_1 = manager('Ayush', 35, 90000, [employee_1])
print(mgr_1.email)
mgr_1.print_emp()
print('this was the old after it new data will be enetered')
mgr_1.add_emp(employee_2)
mgr_1.print_emp()

