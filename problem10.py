"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

num = 2000000
listo = []
counter = 1

sieve = [True for x in range(0,num)]
sieve[0] = False
sieve[1] = False

for i in range(2,int(num**(1/2))+1):
    pointer = i*2
    while pointer < num:
        sieve[pointer] = False
        pointer +=i
    counter+=1

for i in range(0,num):
    if sieve[i] == True:
        # print("bing")
        listo.append(i)
    counter += 1

print(sum(listo))

