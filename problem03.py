"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def primechecker(num):
    primes = []
    for i in range(2, num):
        if num%i == 0:
            primes.append(i)
            answer = 1
            for x in primes:
                answer *= x
            if answer == num:
                return primes

print(max(primechecker(600851475143)))
