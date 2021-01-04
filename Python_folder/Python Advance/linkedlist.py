class node:
    def __init__(self,data):
        self.data = data
        self.next = None;
class linkedlist:
    def __init__(self):
        self.start = None;
    def insertlast(self,value):
        newnode = node(value)
        if(self.start == None)