class LinkedList:
    def __init__(self, head=None): 
        self.head = head 
        self.count = 0 
        return None 
    def insert(self, val, pos):
        counter = 0 
        newNode = Node(val)
        curr1 = self.head
        curr2 = self.head.next 
        while counter < pos: 
            curr1 = curr1.next 
            curr2 = curr.next 
        curr1.next = newNode
        newNode.next = curr2
        return None 
    def append(self, val): 
        return None 
    def insertFront(self, val): 
        newNode = Node(val, self.head)
        return None 
    def removeFirst(self): 
        self.head = self.head.next
        return None 
    def removeNode(self, pos):
        counter = 0 
        curr1 = self.head 
        curr2 = self.head.next 
        while counter < pos - 1:
            curr1 = curr1.next
            curr2 = curr2.next 
        curr2 = curr2.next 
        curr1.next = curr2 
        return None 
        
class Node: 
    def __init__(self, val, next=None):
        self.val = val 
        self.next = None
        return None 
    def getVal(self):
        return self.val 
    def setVal(self, val):
        self.val = val 
        return None 
    def getNext(self):
        return self.next = next 
    def setNext(self, next):
        self.next = next
        return None 
