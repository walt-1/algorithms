# Bubble Sort
# requires many passes over a given list which is O(n^2) in the worst case
# no additional lists are created which is an advantage in terms of space complexity making it O(n)



def bubble_sort(list):
  # setting state of the process
  swapped = True
  # loops over array while state is in swap mode
  while swapped:
    swapped = False
    # iterate over list from index 1 to length of list
    for i in range(1, len(list)):
      # checks prev numbers are greater that current index
      if list[i - 1] > list[i]:
        # performs swap
        list[i], list[i - 1] = list[i - 1], list[i]
        # keeps while loop engaged
        swapped = True
  return list


# from create_array import create_array
# array = create_array()

# print("UNSORTED")
# print(array)

# print("SORTED")
# sorte = bubble_sort(array)
# print(sorte)