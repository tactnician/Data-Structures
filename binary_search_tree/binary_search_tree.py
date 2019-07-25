class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value is None: 
      return False
    if target == self.value:
      return True
    elif target < self.value: 
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    else: 
      return False


  def get_max(self):
    if not self.right: 
      return self.value
    else: 
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
    
    # if self.value is None: 
    #   return None
    # if self.value:
    #   if self.left is None:
    #     return False
    #   return self.left.contains(target)
    # elif target > self.value:
    #   if self.right is None:
    #     return False
    #   return self.right.contains(target)
    # else: 
    #   return False

    
    
    
    # if self.value is None:
    #   return None
      
    #   if not self.left:
    #     self.right.for_each(cb(self.right.value))
    #     return self.value
    #   else: 
    #     self.left.for_each(cb(self.left.value))
    #     return self.value
    #   if not self.right:
    #     return self.value 
    #   else: 
    #     self.right.for_each(cb(self.right.value))
    #     return self.value
    # else:
    #   return cb(self.value)