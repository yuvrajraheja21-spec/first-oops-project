
class Employee:
	def __init__(self, name, age, pay):
		self.name = name
		self.age = age
		self.pay = pay
		self.email = f"{name.lower().replace(' ', '.')}.{age}@company.com"

	def fullname(self):
		return f"{self.name} {self.age}"

	def apply_raise(self):
		self.pay = int(self.pay * 1.04)


employee_1 = Employee('John Doe', 30, 50000)
print(employee_1.email)  # Output: john.doe.30@company.com
print(employee_1.fullname())  # Output: John Doe 30
