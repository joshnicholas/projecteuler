"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

## original (successful) solution:

# num = 20
# divisible = True
# while divisible == True:
#     listo = []
#     for i in range(1,21):
#         result = num%i
#         if result == 0:
#             listo.append(i)
#     if len(listo) == 20:
#         divisible = False
#         print(listo)
#         print(f"num is {num}")
#     else:
#         num += 20

##############

## after googling:

num = 2520
count = 1

while True:
    init = 0
    for i in range(11,21):
        if num%i == 0:
            init += 1
    if init == 10:
        print(num)
        break
    num += 2520

