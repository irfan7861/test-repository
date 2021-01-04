import p1
class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_employee_details (self):
        print("Name of employee ", self.name)
        print("Age of employee ", self.age)

e1 = employee('sameer',32)


e1.show_employee_details()





