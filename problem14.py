"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

dicto = {1:1}
def numberator(num):
    path = [num]
    while num not in dicto:
        if num % 2:
            num = 3 * num + 1
        else:
            num = num / 2
        path.append(num)
    for key, value in enumerate(reversed(path)):
        dicto[round(value)] = dicto[num] + key
    return dicto[path[0]]

for i in range(1,1000000):
    numberator(i)

dicto_values = list(dicto.values())
dicto_keys = list(dicto.keys())
print(dicto_keys[dicto_values.index(max(dicto_values))])