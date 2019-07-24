class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

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
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass