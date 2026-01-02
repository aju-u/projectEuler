# Solution for Question 845: Find D(10^16) where D(n) is the nth positive integer whose digit sum is prime.

# This question was really hard, so I'm going to break down the code.

from functools import lru_cache

# Precompute primes up to 171 (since 9*19=171, or in other words, the sum of digits in the largest 19-digit-number is 171)

maxSUM = 9 * 20     # enough for numbers up to 10^20, which is slightly more than we need
isPrime = [True] * (maxSUM + 1)
isPrime[0] = isPrime[1] = False

for i in range(2, int(maxSUM**0.5) + 1):
    if isPrime[i]:
        for j in range(i*i, maxSUM + 1, i):
            isPrime[j] = False

# Digit DP: count numbers <= X with prime digit sum

# Digit DP is used to stop us from having to brute force 10^16 numbers. Instead, it counts how many numbers there are with certain properties up to a limit (20 digits here).

def countUpTo(X):
    s = str(X)

    @lru_cache(None)
    def dp(pos, tight, digitSum):
        if pos == len(s):
            return 1 if isPrime[digitSum] else 0

        limit = int(s[pos]) if tight else 9
        total = 0

        for d in range(0, limit + 1):
            total += dp(
                pos + 1,
                tight and (d == limit),
                digitSum + d
            )
        return total

    return dp(0, True, 0)

# Find D(n) by binary search
def D(n):
    lo, hi = 1, 10**20
    while lo < hi:
        mid = (lo + hi) // 2
        if countUpTo(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

print("Question 845: " + str(D(10**16)))