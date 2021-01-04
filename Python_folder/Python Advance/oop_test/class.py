class Tv:
    def __init__(self,price,color):
        self.price = price
        self.color = color
    def show_tv_details(self):
        print("Price of tv", self.price)
        print("Color of tv", self.color)
t1 = Tv(30000,"red")
t1.show_tv_details()