"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

listo = []
num = 2

how_many = 10001

count = 1
while len(listo) < how_many:
    prime = []
    for i in range(1,num):
        if num%i == 0:
            prime.append(i)
    if len(prime) < 2:
        print(num)
        listo.append(num)
    num += 1
    
    count +=1

print(count)
print(listo)