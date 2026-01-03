# Solution for Question 4 - Find the largest palindrome made from the product of two 3-digit numbers

def isPalindrome(n): # helper function to check if a number is a palindrome
    return str(n) == str(n)[::-1]

largest = 0

# brute force and check each product
for i in range(100, 1000): 
    for j in range(i, 1000):
        product = i * j
        if isPalindrome(product) and product > largest: # check if product is a palindrome and larger than current largest
            largest = product

print("Question 4: " + str(largest)) # output the largest palindrome found