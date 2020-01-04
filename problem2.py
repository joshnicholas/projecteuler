"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

## original (successful) attempt:

# num1 = 0
# num2 = 1
# fibo = 0
# listo = []   
# while fibo < 4000000:
#     fibo = num1 + num2
#     if fibo%2 == 0:
#         listo.append(fibo)
#     num1 = num2
#     num2 = fibo
    
# print(listo)

# answer = sum(listo)

# print(answer)

################

## revised attempt (after googling):

def fibo(num, limit):
    listo = [0, 1]    
    while num < limit:
        listo.append(listo[-1] + listo[-2])
        shorter = [x for x in listo if x%2==0]
        num = listo[-1]
    return shorter

fiber = fibo(0, 4000000)

print(sum(fiber))

    
