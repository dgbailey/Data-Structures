class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_item(item)
    self.size = self.size + 1
  
  def dequeue(self):
    popped_head = self.storage.get_head().get_value()
    self.storage.set_head(self.storage.get_tail())
    self.size = self.size -1
    return popped_head

  def len(self):
    return self.size
    



class LinkedList():
  def __init__(self, head = None, tail = None):

   self.head = head
   self.tail = tail
   

  def add_item(self, node_value):
    if self.head is None:
      self.head = LinkNode(node_value)

    else:
      if self.tail is None:
        self.tail = LinkNode(node_value)
      else:
        new_node = LinkNode(node_value)
        self.tail.set_next(new_node)
        self.tail = new_node
      

  def get_head(self):
    return self.head

  def set_head(self, new_head):
    self.head = new_head

  def get_tail(self):
    return self.tail
  


class LinkNode():
  def __init__(self,value = None, next = None):
    self.value = value
    self.next = next
     

  def get_value(self):
    return self.value

  def set_value(self,value):
    self.value = value

  def get_next(self):
    return self.next

  def set_next(self,next_value):
    self.next = next_value
    #where do I get this next value
    #it needs to point to another node in the linked list