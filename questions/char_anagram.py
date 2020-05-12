
def group_anagrams(strs):

    # create hash table mapping stings to list of strings
    ana = dict()

    # loop over each word, sort the word, use sorted word as index. if exists in hash table append the current word to 
    # the list at the index of the sorted key. if not in table, create new sorted key and append current word to empty list
    for word in strs:
        sorted_key = ''.join(sorted(word))
        if sorted_key not in ana:
            ana[sorted_key] = [word]
        else:
            ana[sorted_key].append(word)

    return ana.values()


# SYS OUT
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
