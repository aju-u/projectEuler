# Solution for Question 6 - Sum square difference

i = 1
sumOfSquares = 0

while i <= 100:
    sumOfSquares += i ** 2
    i += 1

j = 1
sumTotal = 0

while j <= 100:
    sumTotal += j
    j += 1

answer =  (sumTotal ** 2) - sumOfSquares 

print("Question 6: " + str(answer))