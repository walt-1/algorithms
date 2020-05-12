# Insertion Sort

# Insertion becomes slower as the sorted list grows becaue calculations are made against sorted list
# whereas selection sort computes elements of unsorted list for placement
# The upside of insertion sort is its ability to continually sort lists whereas selection sort would have to resort entire list every time it is executed
# Time is exponential O(n^2)
# Memory is constant O(1)


def insertion_sort(list):
  # loops over sorted sub array incrementing sorted_index
  for sorted_index in range(1, len(list)):
    cur_item = list[sorted_index] # next unsorted item
    insert_index = sorted_index # current index of item
    
    # loops to find insertion index by decrementing insert_index
    while insert_index > 0 and cur_item < list[insert_index - 1]:
      list[insert_index] = list[insert_index - 1] # shifts
      insert_index -= 1 # decrements insert spot

    # inserts item at corrent insertion index
    list[insert_index] = cur_item
  
  return list

# from create_array import create_array
# array = create_array()

# print("UNSORTED")
# print(array)

# print("SORTED")
# sorte = insertion_sort(array)
# print(sorte)