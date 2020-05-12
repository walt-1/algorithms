
def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if not len(prices): return 0

    # with unlimited transactions, every peak and valley can be used to keep
    # track of an aggragate profit by transacting per day.
    max_prof = 0
    for (i, price) in enumerate(prices):
        if i == 0:
            continue

        if price > prices[i-1]:
            max_prof += (price - prices[i - 1])

    return max_prof

p = [5, 11, 3, 50, 60, 90]
m = max_profit(p)
print(m)
