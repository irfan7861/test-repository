#inheritance
# class vehicle:
#     def __main__(self,mileage,cost):
#         self.mileage = mileage
#         self.cost = cost
#
#     def show_vehicle_details(self):
#         print("Mileage of vehicle ", self.mileage)
#         print("Cost of vehicle ", self.cost)
#         print("I am a vehicle")
#
#
# v1 = vehicle(300,50000)

# v1.show_vehicle_details()
#
# class car(vehicle):
#     def show_car_details(self):
#         print("i am a car")
#
# c1 = car(250,800)
#
# c1.show_vehicle_details()
# c1.show_car_details()


class vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("Mileage of vehicle ", self.mileage)
        print("Cost of vehicle ", self.cost)
        print("I am a vehicle")

v1 = vehicle(400,500)
# v1.show_vehicle_details()

class car(vehicle):
    def __init__(self,mileage,cost,tyre,hp):
        super().__init__(mileage,cost)
        self.tyre = tyre
        self.hp = hp
    def show_car_details(self):
        print("Number of tyres ", self.tyre)
        print("Horse power of car ", self.hp)
        print("I am a car")

c1 = car(600,100000,8,9999)
c1.show_vehicle_details()







# class car:
#     def __main__(self,mileage,cost,tyres,hp):
#         super.__main__(mileage,cost)

























