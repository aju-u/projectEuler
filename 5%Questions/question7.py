# Solution for Question 7 - 10,001st Prime number

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

count = 0
num = 1

while count < 10001:
    num += 1
    if isPrime(num):
        count += 1

print(num)