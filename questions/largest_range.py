# Largest Range Problem

# This problem is seeking the longest sequening of ints in a given array.
# One may think that sorting the list and making comparisons would be the best
# approach which would be a time complexity of n log(n).
# A better approach would be to build a hash table and run checks off of accessing values
# in the table

def largest_range(array):
  # init best range
  best_range = []
  # init int holds longest length
  longest_len = 0
  # init hash table
  hash_nums = {}

  # creates hash table with boolean value of true at each key
  for i in array: # O(n)
    hash_nums[i] = True

  # loops over the array in search of the best range
  for cur_num in array: # O(n)
    # checks if value has been visited
    if not hash_nums[cur_num]:
      # move to next item in hash table
      continue

    # currently exploring: set boolean value and length of range
    hash_nums[cur_num] = False
    # sets index for left and right traverse
    cur_len = 1
    # hashtable keys - explores current numbers' siblings
    left = cur_num - 1
    right = cur_num + 1

    # loops while cur num lesser sibling exists in hash table
    while left in hash_nums:
      # visit that value
      hash_nums[left] = False
      # increase length
      cur_len += 1
      # decrement to next sibling
      left -= 1

    # loops while cur num greater sibling exists in hash table
    while right in hash_nums:
      # visit that value
      hash_nums[right] = False
      # increase length
      cur_len += 1
      # decrement to next sibling
      right += 1

    # check cur length
    if cur_len > longest_len:
      # sets longest len for the next iteration
      longest_len = cur_len
      # creates array of the two numbers: 
      # has to recorrect the updated nums that were overrun in the while loop bc a current right num will allow 
      # the next while execution which mutates the num to one that may or may not exist
      best_range = [left + 1, right - 1]

  return best_range

from create_array import create_array

a = create_array(10, 10)
print(a)
ran = largest_range(a)
print(ran)