class Array:
  def __init__(self):
    self.size = 1 
    self.length = 0
    self.arr = [0] * self.size

  def append(self, item):
    if self.size == self.length:
      self.resize()
    self.arr[self.length] = item
    self.length += 1 

  def resize(self):
    self.size = 2 * self.size
    newArr = [0] * self.size 
    for i in range(self.length):
      newArr[i] = self.arr[i]
    self.arr = newArr

  # remove last element of the array
  def remove(self):
    if self.length == 0:
      return "Empty list"
    if self.length > 0:
      self.length -= 1

  #get the value using index
  def getValue(self, i):
    if i < self.length:
      return self.arr[i]

  # replace the value using index

  def repValue(self, i, value):
    if i < self.length:
      self.arr[i] = value
      return 

  def removeSpecificIndex(self, i):
    if i < self.length:
      for j in range(i , self.length-1):
        self.arr[j] = self.arr[j+1]
      self.length -= 1
  

  def print(self):
    for i in range(self.length):
      print(self.arr[i])
    print()


  def __str__(self):
    result = ''
    for i in range(self.length):
      result = result + str(self.arr[i]) + ','

    return '[' + result[:-1] + ']'


  def print1(self):
    result = ''
    for i in range(self.length):
      result = result + str(self.arr[i]) + ','

    return '[' + result [:-1] + ']'





l = Array()

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append('hello')

l.remove()
l.print()

l.getValue(1)

l.repValue(1,50)

l.removeSepIndex(1)

l.print()