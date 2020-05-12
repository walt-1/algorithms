# QUICK SORT

# PIVOTING , PARTITIONIN , RECURSIVE
# divide and conquer algorithm
# requires selecting a medium pivot for best case

# TWO SUBROUTINES
# - split routine
# - partitioning routine - sets pivot posiiton

# TIME: O(n log(n))
# SPACE O(log(n))

from random import randint
def quicksort(list):
  # BASE CASE: returns list of len one bc its sorted by definition
  if len(list) <= 1: return list

  # creates three empty lists holding values smaller, equal, and larger then the pivot
  small, equal, larger = [],[],[]

  # SUBROUTINE 1: defines pivot with random number to keep from selecting worst case pivot everytime
  pivot = list[randint(0, len(list) - 1)]
  
  # SUBROUTINE 2 : loops over list placing current element in correct sub array
  for item in list:
    if item < pivot:    small.append(item)
    elif item == pivot: equal.append(item)
    else:               larger.append(item)
  # returns concat of recursive call on smaller elems, equal elems and recursive call on larger elements 
  # ex. [6, 3, 2] + [3, 3] + [78, 54, 68]
  return quicksort(small) + equal + quicksort(larger)


# SYS OUT
# from create_array import create_array
# array = create_array()

# print("UNSORTED")
# print(array)

# print("SORTED")
# sorte = quicksort(array)
# print(sorte)
