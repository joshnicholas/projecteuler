"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

num1 = 999
num2 = 999
listo = []
while len(str(num1)) >= 3:
    prod = num1 * num2
    if (str(prod)[0] == str(prod)[-1]) & (str(prod)[1] == str(prod)[-2]) & (str(prod)[2] == str(prod)[-3]):
        listo.append(prod)
        num2 -= 1
    else:
        num2 -= 1
        if len(str(num2)) < 3:
            num1 -= 1
            num2 = 999

print(max(listo))