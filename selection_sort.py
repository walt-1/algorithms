# Selection Sort

# The original list is split up into two sections, sorted and unsorted
# O(n^2) in all cases, because every item in the list has to be checked and compared
# All processes are done in place O(n)
# uses two pointers, one for current one for minimum num found. each time the inner loop sets the next smallest number, it is swapped with the current num in outer loop

def selection_sort(list):
  # sets sorted array length to 0
  sorted_len = 0
  # loops while the sorted length is less than length of array
  while sorted_len < len(list):
    # initialize index of minimum value to -1 in place of value yet to be found
    min_index = None;
    # loops over list indexed after sorted indexes aka the remaining items in list
    for i, elem in enumerate(list[sorted_len:]):
      # checks if current index has smallest item so far
      if min_index == None or elem < list[min_index]:
        # sets index of min value to sorted array: uses addition of local index and sorted index to get global index
        min_index = i + sorted_len
    
    # builds sorted array
    # swaps value of smallest item found from list to the end of sorted list
    list[sorted_len], list[min_index] = list[min_index], list[sorted_len]
    # increment sorted
    sorted_len += 1
  
  # returns sorted list 
  return list


# from create_array import create_array
# array = create_array()

# print("UNSORTED")
# print(array)

# print("SORTED")
# sorte = selection_sort(array)
# print(sorte)