# Solution for Question 3 - Find the largest prime factor of a number

n = 600851475143 # the number to find the largest prime factor of
factor = 2

while factor * factor <= n: # only need to check factors up to the square root of n
    if n % factor == 0:
        n //= factor # divide n by factor until it no longer divides evenly
    else:
        factor += 1

print("Question 3: " + str(n))  # n is now the largest prime factor