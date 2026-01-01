# Question 112: Bouncy Numbers

def isBouncy(n):
    digits = list(str(n))
    increasing = decreasing = True

    for i in range(1, len(digits)):
        if digits[i] > digits[i - 1]:
            decreasing = False
        elif digits[i] < digits[i - 1]:
            increasing = False

    return not (increasing or decreasing)

count = 0
n = 1

while True:
    if isBouncy(n):
        count += 1
    if count / n == 0.99:
        break
    n += 1

print("Question 112: " + str(n))