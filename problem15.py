"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

def unsquarer(side):
    listo = [1 for x in range(side)]
    for x in range(len(listo)):
        for y in range(x):
            listo[y] = listo[y] + listo[y-1]
        listo[x] = listo[x-1] * 2
    print(listo[-1])

unsquarer(20)