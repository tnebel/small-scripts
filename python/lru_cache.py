class node:
  def __init__(self, data = None):
    self.data = data
    self.next = None
    self.prev = None

class linked_list:
  """ doubly linked list """
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def prepend(self, new_node):
    if self.head == None:
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next  = self.head
    self.head = new_node
    self.size+=1

  def print_list(self):
    curr = self.head
    while not (curr == None):
      print curr.data
      curr = curr.next

  def remove(self, n):
    if self.head == n:
      self.head = n.next
    else:
      n.prev.next = n.next
    if self.tail == n:
      self.tail = n.prev
    else:
      n.next.prev = n.prev
    self.size-=1

class lru_cache:
  """ provides a lru cache, which evicts the least recently used
      item once capacity is reached. The cache is backed by a 
      linked list and a hash map. This allows amortized constant time
      lookup, insertion, and removal """
  def __init__(self, cap = 10):
    self.ll = linked_list()
    self.mapping = {}
    self.capacity = 10

  def insert(self, data):
    if data in self.mapping:
      return False
    new_node = node(data)
    self.ll.prepend(new_node)
    self.mapping[data] = new_node
    if self.ll.size > self.capacity:
      last = self.ll.tail
      del self.mapping[self.ll.tail.data]
      self.ll.remove(self.ll.tail)
    return True

  def lookup(self, data):
    if data not in self.mapping:
      return None
    n = self.mapping[data]
    self.ll.remove(n)
    self.ll.prepend(n)
    return n.data

  def print_cache(self):
    self.ll.print_list()

