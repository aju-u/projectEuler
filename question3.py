# Solution for Question 3 - Find the largest prime factor of a number

n = 600851475143
factor = 2

while factor * factor <= n:
    if n % factor == 0:
        n //= factor
    else:
        factor += 1

print("Question 3: " + str(n))