class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    # self.storage =  [item] + self.storage
    
  
  def dequeue(self):
    if len(self.storage) is 0:
      return None
    else:
      return self.storage.pop()
    # self.storage = self.storage[:len(self.storage) -1]
    

  def len(self):
    return len(self.storage)
    