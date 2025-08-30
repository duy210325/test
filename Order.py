class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id, self.name, self.price }"
    
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class dataList:
    def __init__(self):
        self.head = self.tail = None
    
    def enqueue(self, id, name, price):
        new_node = Node(Item(id, name, price =0 ))
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def display(self):
        print("Data List:")
        if self.head is None:
            print('Empty')
        current = self.head
class RequestQueue: 
    def dequeue(self):
        tmp = None
        if self.head == None:
            self.head = self.tail = None
        
        tmp = self.head
        self.head = self.head.next
        return tmp
class ComputerStore:
    def __init__(self):
        self.data = dataList()     
    def purchase(self,data): 
        money = 0
        current = self.