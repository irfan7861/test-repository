class Employee:
    company = "Google"

irfan = Employee()
sameer = Employee()
print(irfan.company)
print(sameer.company)
Employee.company = "YouTube"
print(irfan.company)
print(sameer.company)