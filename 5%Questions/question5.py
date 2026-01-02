# Solution for Question 5 - Smallest multiple

import math

lcm = 1

for i in range(1, 21):
    lcm = lcm * i // math.gcd(lcm, i)


print("Question 5: " + str(lcm))