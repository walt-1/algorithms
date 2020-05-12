def first_nonrepeat(s): # O(n)
    # creates set alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'    
    idx_first_nonrep = [s.index(l) for l in letters if s.count(l) == 1]
    # 1.loops through letters 
    # 2.asserts that the current letter in alpha occurs once in the input string
    # 3.appends index of single occurance char
    # 1.for let in letters:
        # 2.if s.count(let) == 1:
            # 3.idx_first_nonrep.append(s.index(let))
            
    # returns smallest num in array of indexes bc the question asks for first occurance of non repeat
    # asserts that array has items in it else returns -1
    return min(idx_first_nonrep) if len(idx_first_nonrep) > 0 else -1

print(first_nonrepeat("aaadddbbbbilccc"))
