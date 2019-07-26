"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)#insertnewhead
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):

    if self.length == 0:
      self.tail = ListNode(value)
      self.head = ListNode(value)
      self.length +=1
    
    else:
      current_head = self.head
      #insert before current head
      current_head.insert_before(value)
      self.head = current_head.prev
      self.length +=1


  def remove_from_head(self):
    #kind of like delete

     if self.length == 0:
      removed_head = self.tail
      self.head = None
      self.tail = None

     elif self.length == 1:
      removed_head = self.tail
      self.head = None
      self.tail = None
      self.length -=1
      return removed_head.value

     else:
      removed_head = self.head
      self.head.delete()
      self.head = removed_head.prev
      self.length -=1
      return removed_head

  def add_to_tail(self, value):

    if self.length == 0:
      self.tail = ListNode(value)
      self.head = ListNode(value)
      self.length +=1

    else:

      current_tail = self.tail
      self.tail.insert_after(value)
      self.tail = current_tail.next
      self.length +=1
      

  def remove_from_tail(self):
    if self.length is 1:
      removed_tail = self.tail
      self.head = None
      self.tail = None
      self.length -=1
      return removed_tail.value
    else:
      removed_tail = self.tail
      self.tail.delete()
      self.tail = removed_tail.prev
      self.length -=1
      return removed_tail.value
    

  def move_to_front(self, node):
    
    node.next = self.head
    self.head = node
    

  def move_to_end(self, node):
    curr_tail = self.tail
    node.prev = curr_tail
    self.tail = node
    

  def delete(self, node):
   

    if self.length == 1:
        if self.head.value == node.value:
          self.head = None
          self.tail = None
          self.length -=1

    elif self.length == 2:
      if self.head.value == node.value:

          
          self.head = self.tail
          
          self.length -= 1

      elif self.tail.value == node.value:

          self.tail = self.head
          self.length -= 1

      elif self.head.value == node.value and self.tail.value == node.value:
          self.tail, self.head = None, None
          self.length -= 1


    else:

      list_start = self.head

      if self.head.value == node.value:

          self.head = self.head.next

      if self.tail.value == node.value:
          self.tail = self.tail.prev

      while list_start is not None:
        comparison_node = list_start

        if comparison_node.value == node.value:
          comparison_node.delete()
          self.length -=1
        list_start = list_start.next


    
    
  def get_max(self):

    if self.length == 0:
      return 0

    elif self.head:
      curr_max = self.head.value
      curr_node = self.head
      while curr_node != None:

        
        comparision_value = curr_node.value

        if comparision_value > curr_max:
          curr_max = comparision_value

        curr_node = curr_node.next


      return curr_max

