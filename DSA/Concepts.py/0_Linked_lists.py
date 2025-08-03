# creating a node
class Node:
    #creating objects
    def __init__(self, data=None, next = None):
        self.data = data #created data object
        self.next = next # created next object
class LinkedList:
    def __init__(self):
        self.head = None
            