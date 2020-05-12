
def inter(nums, numss):
    
    # create two hash maps
    m1 = dict()
    m2 = dict()

    # loop through nums and add occurances of each item to hash one
    for n in nums:
        # get method will either return existing value or return what is trying to be set
        # if a value has been set, it is incremented in place else it is set to 0
        m1[n] = m1.get(n, 0) + 1
            
    # loop through numss and add occurances of each item to hash two
    for m in numss:
        m2[m] = m2.get(m, 0) + 1

    # create interestion hash map
    intersection = dict()
    # loop through nums again
    for i in m1:
        # check if each item is in map two
        if i in m2:
            # if it is, calc min occurances of map one and two and set to intersetion map
            intersection[i] = min(m1[i], m2[i])

    result = list()
    # loop through intersetion map and append num of keys for each ket to the result
    for j in intersection:
        result += ([j] * intersection[j])
    
    return result 


# SYS OUT
intersection = inter([4, 9, 5], [9, 4, 9, 8, 4])
print(intersection)
