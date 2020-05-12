# Two Sum Problem
# given array and target - take two entries equal the target.clear
from create_array import create_array
arr = create_array()

# Brute Force
# T = O(n ^ 2)
# S = O(1) no aux data structures
def two_sum_bf(array, target):
  for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
      if array[i] + array[j] == target:
        return [i, j]
  return "not found"

# print(two_sum_bf(arr, 21))

# Hash Table 
# T = O(n)
# S = 0(n) bc of created ds
def two_sum_ht(array, target):
  # defines hash table
  ht = dict()
  
  for i in range(len(array)):
    # checks if current array item exists in the hash table
    if array[i] in ht:
      # returns array of indexes: index of value to reach target as hash value 
      # and cur index 
      return [ ht[array[i]], i ]
      
    else:
      # builds hash table - keys are the num needed to reach target
      # For a given number in the array, alg takes the dif btw target and number 
      # { what is needed: value needed for return }
      ht[target - array[i]] = i # could be current index - could be the value at current index
      
  return "not found"

# print(two_sum_ht(arr, 21))


# Assumes Sorted 
# T = 0(n)
# T = 0(1)
arr.sort()
def two_sum_sorted(s_arr, target): # S = O(1)
  inc = 0
  dec = len(s_arr) - 1

  while inc <= dec: # O(n)
    if s_arr[inc] + s_arr[dec] == target:
      return [inc, dec]
    elif s_arr[inc] + s_arr[dec] < target:
      inc += 1
    else:
      dec -= 1
  return "not found"
