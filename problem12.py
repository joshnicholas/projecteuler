"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

def triangler2(n):
    n = n
    num = (n*(n+1))/2
    return round(num)

triangles = [triangler2(i) for i in range(1,100000)]

def factoriser(num):
    factors = 2*sum(num%i==0 for i in range(1,int((num**(1/2))) +1 ))
    if int(num**(1/2))**2 == num:
        factors -= 1
    return(factors)

for i in triangles:
    num = factoriser(i)
    if num >= 500:
        print(f"######## {i}")
        break