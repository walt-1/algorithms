# Stack to convert integer into binary format
# the stack keeps track of the remainders as the number is continuously divided by two

class stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)
    
  def pop(self):
    return self.items.pop()
    
  def get_stack(self):
    return self.items

  def is_empty(self):
    return self.items == []

  def peek(self):
    if not self.is_empty():
      return self.items[-1]


def div_by_two(num):
  # creates stack instance
  s = stack()
  
  # loops over the num while it is greater than zero
  while num > 0:
    ## creates local var and sets value to the remainder of the division
    rem = num % 2
    ## pushes remainder onto stack
    s.push(rem)
    ## performs division '//' takes floor
    num = num // 2

  # creates string that hold bin rep
  bin_rep = ""
  
  # loops while the stack is not empty
  while not s.is_empty():
    ## sets bin value with += of popped stack item to build the string
    bin_rep += str(s.pop())

  # returns string binary rep
  return bin_rep


# Calls method
print(div_by_two(2137))