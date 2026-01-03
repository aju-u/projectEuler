# Solution for Question 6 - Sum square difference

i = 1
sumOfSquares = 0

while i <= 100: 
    sumOfSquares += i ** 2 # add the square of i to the total sum of squares
    i += 1

j = 1
sumTotal = 0

while j <= 100:
    sumTotal += j # add j to the total sum
    j += 1

answer =  (sumTotal ** 2) - sumOfSquares # square of the sum minus the sum of the squares

print("Question 6: " + str(answer))