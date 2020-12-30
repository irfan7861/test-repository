class Employee:
    company = "Google"

irfan = Employee()
sameer = Employee()
print(irfan.company)
print(sameer.company)
Employee.company = "YouTube"
print(irfan.company)
print(sameer.company)

class phone:
    def make_call(self):
        print("I am making a call")
    def play_game(self):
        print("I am playing game")


p1 = phone()

p1.make_call()

p1.play_game()



class laptop:
    def lap_ram(self):
        print("4GB ram")
    def lap_hdd(self):
        print("1TB Memory")
    def lap_cpu(self):
        print("I3 processor")
    def lap_graphics(self):
        print("2GB Nvidea")
#
#
l1 = laptop()


l1.lap_ram()
l1.lap_graphics()
l1.lap_cpu()
l1.lap_hdd()


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


e1.show_employee_details()




class tv:
    def __init__(self,screen,brand,price):
        self.screen = screen
        self.brand = brand
        self.price = price

    def show_tv_details(self):
        print("Size of screen ", self.screen)
        print("Brand of tv ", self.brand)
        print("Price of tv ", self.price)

t1 = tv("32 inch", "samsung", 20000)

t1.show_tv_details()















