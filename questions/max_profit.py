# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

def max_proft(prices):
    # init min price is set to inf
    min_price = float("-inf")
    # init max profit is zero
    maxprof = 0

    # iterate through every price
    for (i, price) in enumerate(prices):
        # check if cur price is less than cur min price
        if price < min_price:
            # sets min price
            min_price = price
        # checks diff between cur price and min price - if that is greater than cur max profit, set max profit
        elif price - min_price > maxprof:
            max_proft = price - min_price
        
    # return max profit
    return maxprof
