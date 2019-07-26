
class Heap:
  def __init__(self):
    self.storage = []
    

  def insert(self, value):
   self.storage.append(value)
   appended_item_index = len(self.storage) -1
   self._bubble_up(appended_item_index) 

  #then 

  def delete(self):

    if len(self.storage) == 1:
      return self.storage.pop(0)

    else:

      deleted_item = self.storage[0]
      last_item = -1
      self.storage[0] = self.storage.pop(last_item)
      print("new root",self.storage[0])
      print("new storage",self.storage)
      self._sift_down(0)
      return deleted_item

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    '''moves the element at the specified index "up"
       the heap by swapping it with its parent if the 
       parent's value is less than the value at the specified
       index.'''
  
    parent = self.storage[(index -1)//2]
    child = self.storage[index]
    

    if index == 0:
     
      return True

    elif parent < child:
    
      self.storage[(index -1)//2], self.storage[index] = self.storage[index], self.storage[(index -1)//2]
      self._bubble_up((index -1)//2)




  def _sift_down(self, index):
    '''grabs the indices of this element's children and determines 
       which child has a larger value. If the larger child's value
       is larger than the parent's value, the child element is swapped
       with the parent'''
    parent = self.storage[index]
    
    if ((2*index + 1) < len(self.storage))  and ((2*index + 2) < len(self.storage)):
      right_child = self.storage[(2*index +2)]
      left_child = self.storage[(2*index + 1)]

      if left_child > right_child:
        print("left child wins")
        if left_child > parent:
          print("left child greater than parent")
          self.storage[index], self.storage[(2*index + 1)] = self.storage[(2*index + 1)], self.storage[index]
          print("swapped", self.storage)
          self._sift_down((2*index + 1))

      elif right_child > left_child:
        print("left child wins")
        if right_child > parent:
          print("right child greater than parent")
          self.storage[index], self.storage[(2*index +2)] = self.storage[(2*index +2)], self.storage[index]
          print("swapped", self.storage)
          self._sift_down((2*index + 2))

      elif right_child == left_child:
        print(" child TIE!")
        
        self.storage[index], self.storage[(2*index +2)] = self.storage[(2*index +2)], self.storage[index]
        print("swapped", self.storage)
        self._sift_down((2*index + 2))

    elif len(self.storage) == 2:
      if parent < self.storage[1]:
        self.storage[0],self.storage[1] = self.storage[1],self.storage[0]

    # elif (2*index + 1) < len(self.storage) and :
    #   if self.storage[2*index + 1] > self.storage[index]:
    #     self.storage[index], self.storage[(2*index + 1)] = self.storage[(2*index + 1)], self.storage[index]


    # elif 2*index + 1 < len(self.storage)
    #   left_child = self.storage[2*index + 1]
    #   if left_child > parent:
      
    #     parent, left_child = left_child, parent
    #     self._sift_down(2*index + 1)

  

    

    

    #else last item is the new max and nothing needs to be done





