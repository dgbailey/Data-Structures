class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_item(item)
  
  def dequeue(self):
    pass

  def len(self):
    pass


class LinkedList():
  def __init__(self, head = None, tail = None):

   self.head = head
   self.tail = tail
   

  def add_item(self, node):
    if self.head is None:
      self.head = LinkNode()

    else:
      self.tail = node

  def get_head(self):
    return self.head

  def get_tail(self):
    return self.tail
  


class LinkNode():
  def __init__(self,value = None, next = None):
    self.value = value
    self.next = next
     

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next
    #where do I get this next value
    #it needs to point to another node in the linked list