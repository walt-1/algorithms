# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def count_primes(n):
    if n < 3:
        return 0
    # defines and initializes primes as an array of len n with '1' placeholders to set up summation in return
    primes = [1] * n
    # sets first two items in list to '0' bc 1 and 2 are not prime
    primes[0] = primes[1] = 0
    # sets index to start at third position
    index = 2
    # there are no primes greater than the square of the current number
    while index * index < n:
        # checks if num has not been looked at or is prime
        if primes[index] == 1:
            # uses array splicing to assign an array of zero, length of calc, to factors of current index
            # [4:37:2] -> [start on 4: til 37: incr by 2]
            primes[index * index:n:index] = [0] * (1 + (n - index * index - 1) // index)
        # increases m by one if m is 2 else increments by 2
        index += 1 if index == 2 else 2

    # returns the sum of 1s in the prime array
    return sum(primes)

count_primes(37)
