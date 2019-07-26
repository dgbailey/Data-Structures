class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __repr__(self):
      if self.right is not None:
          fmt = '{}({value!r}, {left!r}, {right!r})'
      elif self.left is not None:
          fmt = '{}({value!r}, {left!r})'
      else:
          fmt = '{}({value!r})'

      return fmt.format(type(self).__name__, **vars(self))
      
  def insert(self, value):
    if value: # if valid value
      if value >= self.value: #check gt root
        if self.right:#if there is a child, check if child is a parent
             return self.right.insert(value)
        else:
          self.right = BinarySearchTree(value)

      elif value < self.value:
        if self.left:
            return self.left.insert(value)
        else:
          self.left = BinarySearchTree(value)
          
    else:
     raise Exception("Value cannot be None")

     

  def contains(self, target):
    if target:
      if self.value:
        if self.value == target:
          return True

        elif self.value > target:
          if self.left:
            return self.left.contains(target)
          else:
            return False

        elif self.value < target:
          if self.right:
            return self.right.contains(target)
          else:
            return False

      else:
        return False
    
    else:
      raise Exception("Search Value Cannot be None")

  def get_max(self):
    if self.value:
      if self.right:
        if self.right.value > self.value:
          return self.right.get_max()
        else:
          return self.value
      else:
        return self.value

    else:
      return False

  def for_each(self, cb):
    
    cb(self.value)
  
    if self.left:
      return self.left.for_each(cb)

    if self.right:
      return self.right.for_each(cb)
