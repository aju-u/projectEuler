# Solution for Question 5 - Smallest multiple

import math 

lcm = 1

for i in range(1, 21):
    lcm = lcm * i // math.gcd(lcm, i) # update lcm using the formula lcm(a, b) = abs(a*b) // gcd(a, b), where "gcd" is the greatest common divisor


print("Question 5: " + str(lcm))