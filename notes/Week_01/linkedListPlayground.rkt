#lang dssl2


# The headerless linked list 
def cons: 
	let value
	let next

cons( 1, 
      None ) 
cons( 1, 
      cons(2, None) 
      ) 

# The headerful linked list 
class SLL: 
  let head 
  def __init__(self):
    self.head = head 
  def get_front(self):
    if cons?(self.head): 
      return self.head.val 
    error('no element in list')
  def getNode(self, pos):
    let curr = self.head 
    while not curr == None: 
      if n == 0: 
        return curr.data
      curr = curr.next 
      n = n - 1 
    error('element does not exist') 
  def findNode(self, n): 
    let curr = self.head 
    while not curr == None: 
      if n == 0: 
        return curr
      curr = curr.next
      n = n - 1 
    error('invalid index')

  def setNode(self, val, n):   
    let currentNode = findNode(n)
    currentNode.val = val 
    return None 
  def getCount(self): 
    counter = 0 
    curr1 = self.head
    while curr1.next != None: 
      counter += 1 
    return counter 
     


