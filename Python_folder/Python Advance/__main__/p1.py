class employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_employee_details (self):
        print("Name of employee ", self.name)
        print("Age of employee ", self.age)
        print("Salary of employee ", self.salary)
        print ("Gender ofemployee ", self.gender)

e1 = employee('sameer',32,50000,'male')
if __name__ == '__main__':
    e1.show_employee_details()
