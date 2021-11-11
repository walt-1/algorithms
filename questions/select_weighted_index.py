# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
# (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), 
# and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

def select_weighted_index(weights):
    # initialize accumulated list
    ac_list = []
    # init accumulator var 
    ac = 0
    # loop through list of weights and add each value to the accumulated var
    for w in weights:
        # set total sum from accumulator var
        ac += w
        ac_list.append(ac)
    
    return pick_int(ac_list)

# function to select random index given weigh calc
def pick_int(ac_list):
    # generate random num using ac value
    from random import randint
    rand = randint(0, ac_list[len(ac_list) - 1])
    
    # init boundary vars
    lo, hi = 0, len(ac_list)
    # search accumulated list to find number
    while lo < hi:
        m = lo + (hi - lo)//2
        if rand > ac_list[m]:
            lo = m + 1
        else:
            hi = m
    
    # return lo index 
    return lo

print(select_weighted_index([1, 2, 5, 7, 21]))
