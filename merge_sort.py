# Merge Sort 
# Recursive divide and conquor algorithm splitting a given list into n arrays
# Time: O(n log n) -  divide log(n) + recombination = n
# Space: O(n)
# does log n merge steps because each merge step doubles the list size and does n work for each merge because it has to look at every item
# better for large data sets than small

# merge sort 

def merge_sort(list):
  # a list of zero and one elements is sorted 
  if len(list) <= 1: return list

  # splits list in half and calls itself recursively on each half
  left = merge_sort(list[:len(list)/2])
  right = merge_sort(list[len(list)/2:])
  # merges the sublists
  return _merge(left, right)

def _merge(left, right):
  # creates array that will contain two sub arrays
  single_list = list()
  # creates index for left and right halves
  l = r = 0

  # loop over array until reaching the end of one of them
  while l < len(left) and r < len(right):
    # checks item at the top of each array
    # append smaller to return list
    # incement index
    if left[l] < right[r]:
      single_list.append(left[l])
      l += 1
    else:
      single_list.append(right[r])
      r += 1
  
  # push remaining elements of a sub array onto the return list
  if l == len(left): 
    # iterates over remaining items and appends them to list
    single_list.extend(right[r:])
  else: 
    single_list.extend(left[l:])
  
  # returns array
  return single_list



def divide(list):
  if len(list) <= 1: return list
  
  left = divide(list[:len(list) / 2])
  right = divide(list[len(list) / 2:])

  return _combine(left, right)

def _combine(left, right):
  single_list = list()

  l = r = 0

  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      single_list.append(left[l])
      l += 1
    else:
      single_list.append(right[r])
      r += 1
  
  if l == len(left):
    single_list.extend(right[r:])
  else:
    single_list.extend(left[l:])

  return single_list


from create_array import create_array
array = create_array()

print("UNSORTED")
print(array)

print("SORTED")
sorte = divide(array)
print(sorte)