# Max Profit with K Transactions

# Calcs max profit of a stock given input of amount of transactions where trans=buy then sell
# Can only buy one share at a time

# Ex. [5, 11, 3, 50, 60, 90] where k = 2
# An.  B  S   B          S   max-prof = $93.00

# TIME: O(n^2 * k) if applying a profit formula to each possible transation
# but if the same work is being done repeating, there usually is a way to
# cache a value to save compute time
# SPACE: O(n) - only needing to look at two rows at a time, never the entire matrix

# Dynamic programming to get O(n*k)
# Build table that leads to solution
# returns 2D array
def max_profit(prices, k):
    if not len(prices):
        return 0
    # matrix rows are trans and cols are daily closing-prices [possible-transactions][day]
    # first transaction is 0 so no profit will ever be generated [[0,0,0] ...]
    # first col will always be 0 bc no profit can be generated within a day - profits only come from prev day [[0, ..],[0, ..] ..]
    # continue on to calc diff of each price to get profit for each item in the matrix

    # SPACE O(n*k)
    # matrix_prof = [[0 for eod in prices] for tran in range(0, k + 1)]
    
    # SPACE O(n)
    even_row = [0 for eod in prices]
    odd_row = [0 for eod in prices]
    def is_even(trans): return trans % 2 == 0

    # loop through allowed num transactions
    for tran in range(1, k + 1): # [[0,0] ..]
        cur_maxprof = float("-inf")
        
        if is_even(tran):
            cur_total_profit = even_row
            prev_total_profit = odd_row
        else:
            cur_total_profit = odd_row
            prev_total_profit = even_row
            
        # loop through each price to make a profit calc
        for eod in range(1, len(prices)):  # [[0, ..], [0, ..] ..]
            last_tran_last_prof_minus_eoyd = prev_total_profit[eod - 1] - prices[eod - 1]
            
            this_tran_last_prof = cur_total_profit[eod - 1]
            
            cur_maxprof = max(cur_maxprof, last_tran_last_prof_minus_eoyd)
            
            cur_maxprof_plus_eod_price = cur_maxprof + prices[eod]
            
            # assigns the max profit to matrix
            cur_total_profit[eod] = max(
                this_tran_last_prof, cur_maxprof_plus_eod_price)

    return even_row[-1] if is_even(k) else odd_row[-1]


p = [5, 11, 3, 50, 60, 90]
k = 1
m = max_profit(p, k)
print(m)
