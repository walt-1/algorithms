# Nth Fib
# fib(n) = fib(n-1) + fib(n-2) for n > 2
from math import math

# Basic Recursive
# T = O(2^n)
# S = O(n) - recursive calls by nature generate a call stack for each nest calc -> n
def nth_fib_basic(n):
  # two base cases that set the first 
  if n == 2:
    return 1
  elif n == 1:
    return 0
  # recursive call using the sequence to return
  else:
    return nth_fib_basic(n - 1) + nth_fib_basic(n - 2)


# Recursive With Memoize
# T = O(n) - only has to visit a num in the fib sequence once
# S = O(n)
def nth_fib_mem(n, mem={1:0, 2:1}):
  if n in mem:
    return mem[n]
  else:
    mem[n] = nth_fib_mem(n - 1, mem) + nth_fib_mem(n - 2, mem)
    return mem[n]


# Iterative 
# T = O(n)
# S = O(1)
def nth_fib_it(n):
  lastTwo = [0, 1]
  count = 3
  
  while count <= n:
    next = lastTwo[0] + lastTwo[1]
    lastTwo[0] = lastTwo[1]
    lastTwo[1] = next
    count += 1
  
  return lastTwo[1] if n > 1 else lastTwo[0]



def fib_math(n):
    sqrt5 = math.sqrt(5)
    fibn = ((1+sqrt5)/2)**(n+1) - ((1-sqrt5)/2)**(n+1)
    return int(fibn/sqrt5)

def print_fib(n):
  s = list()
  i = 1
  while i >= 1 and i <= n:
    # fib = nth_fib_basic(i)
    s.append(nth_fib_it(i))
    i += 1
  print(s)
  

print_fib(6)
