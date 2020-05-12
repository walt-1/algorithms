# STACK Data Structure
# Works similar to a stack of objects like books where 
# pushing and popping act upon the top item in the stack
"""
cur_item = list.pop() : D

C
B
A
"""

class stack:
  def __init__(self):
    # creates an empty list
    self.items = list()
  
  # params item
  def push(self, item):
    # places an item at the end of the list or top of the stack
    self.items.append(item)
  
  # takes no additional params
  def pop(self):
    # returns item at the end of the stack
    return self.items.pop()
  
  def get_stack(self):
    return self.items

  def is_empty(self):
    return self.items == []
  
  def peek(self):
    if not self.is_empty():
      return self.items[-1]

# s = stack()
# print(s.is_empty())
# s.push("A")
# s.push("B")
# print(s.get_stack())
# s.push("C")
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# print(s.is_empty())
# print(s.peek())

# SOLVE: balanced parenthesis?
# Ex. (), ()(), (({[]})) <- bal
# ... ((), {{{)}], [][]]] <- not bal

# helper function to return if the parens correspond
def is_match(p1, p2):
  if p1 == '(' and p2 == ')':
    return True
  elif p1 == '[' and p2 == ']':
    return True
  elif p1 == '{' and p2 == '}':
    return True
  else:
    return False

# CHECK PAREN BALANCE
# 1. create function that accepts string
def is_paren_balanced(parens):
  # 2. creates instance of stack
  st = stack()
  # 3. defines boolean var that will be returned after calc
  is_bal = True
  # 4. creates index var keep track of where the loop iterations
  index = 0

  # 5. creates loop that runs while the index is less than paren len and string is balanced
  while index < len(parens) and is_bal:
    # 6. grabs paren char
    cur_paren = parens[index]

    # 7. checks if paren is opener
    if cur_paren in '{[(':
      # 8. pushes paren onto stack
      st.push(cur_paren)
    else:
      # 9. checks if stack is empty
      if st.is_empty():
        # 10. updates state of function to unbalanced
        is_bal = False
      else:
        # 11. pops item off nonempty stack
        top = st.pop()
        # 12. check if last paren and cur_paren correspond
        if not is_match(top, cur_paren):
          # 13. set state to false
          is_bal = False
    
    # 14. increment index
    index += 1
  
  # 15. checks if stack is empty and is balanced return state
  if st.is_empty() and is_bal:
    return True
  else:
    return False

# BAL
# print("Balaced String?")
# print(is_paren_balanced("(({[]}))"))
# UNBAL
# print("Unbalaced String?")
# print(is_paren_balanced("{{{)}]"))

# REVERSE STRING
# accepts string and stack object
def reverse_string(string, stack):
  # loop over chars in string
  for index in range(len(string)):
  # push char onto the stack one by one
    stack.push(string[index])

  # init string to build 
  rev_str = ""
  # loop over stack while it has chars
  while not stack.is_empty():
    # pop char off of stack and concat to rev_str
    rev_str += stack.pop()

  return rev_str

# rev_stack = stack()
# input_str = "Hello"
# print("\nReverse String: " + input_str)
# print(reverse_string(input_str, rev_stack))



