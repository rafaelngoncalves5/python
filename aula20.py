# Aula 20

# Sets são uma estrutura de dados não ordenadas e que não possuem dados repetidos

# Podemos criar um set com chaves ou passando uma lista em seu método construtor

# Forma 1
my_set = {"Item 1", "Item 2"}
my_set2 = set(["Item 3", "Item 4"])

# Set comprehension
my_set_3 = {i for i in range(1, 4) if True}

# Frozenset é basicamente um set, não alterável

# Define-se um frozenset da mesma forma que definimos um set
my_frozenset = frozenset(my_set)

'''
Métodos básicos do set
    - add() -> Adiciona um item no set
    - update() -> Adiciona vários itens num set
    - remove() -> Remove um item do set, se ele existir
    - discard() -> Mesma coisa do remove, mas não retorna excessão se o item for inexistente
'''

# Usando filas

'''
class Queue:
 def __init__(self):
   self.head = None
   self.tail = None
   self.size = 0
 
 def enqueue(self, value):
   if self.has_space():
     item_to_add = Node(value)
     print("Adding " + str(item_to_add.get_value()) + " to the queue!")
     if self.is_empty():
       self.head = item_to_add
       self.tail = item_to_add
     else:
       self.tail.set_next_node(item_to_add)
       self.tail = item_to_add
     self.size += 1
   else:
     print("Sorry, no more room!")
 
 def dequeue(self):
   if self.get_size() > 0:
     item_to_remove = self.head
     print(str(item_to_remove.get_value()) + " is served!")
     if self.get_size() == 1:
       self.head = None
       self.tail = None
     else:
       self.head = self.head.get_next_node()
     self.size -= 1
     return item_to_remove.get_value()
   else:
     print("The queue is totally empty!")
  def peek(self):
   if self.size > 0:
     return self.head.get_value()
   else:
     print("No orders waiting!")
  def get_size(self):
   return self.size
 def is_empty(self):
   return self.size == 0
'''

# Exemplo com stack

'''
from node import Node
 
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
 
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("All out of space!")
 
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
 
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
 
 
  def is_empty(self):
    return self.size == 0
'''