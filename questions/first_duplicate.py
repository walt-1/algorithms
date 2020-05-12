def first_duplicate(arr):
    for (i, value) in enumerate(arr): # O(n)
        # uses current num value minus one as an 
        # index to access another value in 
        # the array to check if its been visited 
        if arr[abs(arr[i]) - 1] < 0: 
            return abs(value)
        else:
            arr[abs(arr[i]) - 1] = -(arr[abs(arr[i]) - 1])

    return -1 


first_dup = first_duplicate([1, 2, 3, 2, 5])
print(first_dup)