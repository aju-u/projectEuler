# Solution for Question 2 - Sum of even Fibonacci numbers not exceeding four million

a, b = 1, 2 # store first two Fibonacci numbers into variables
total = 0

while a <= 4_000_000: # loop until the Fibonacci number exceeds four million
    if a % 2 == 0:
        total += a
    a, b = b, a + b # update a and b to the next two Fibonacci numbers

print("Question 2: " + str(total)) # output the total sum of even Fibonacci numbers