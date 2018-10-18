import math


def valid(a, b, c):
    if a <= b and b < c:
        if c == math.sqrt((a**2 + b**2)):
            return True

    return False


import time

start = time.time()

triangles = []
highest = (0, 0)

for perimeter in range(1, 1001):
    solutions = 0
    if perimeter % 3 == 0:
        for a in range((perimeter / 2) + 1, 0, -1):
            for b in range((perimeter / 2) + 1, 0, -1):
                c = perimeter - a - b

                if valid(a, b, c):
                    solutions += 1
                    # triangles.append((perimeter, (a, b, c)))

        if solutions > highest[1]:
            highest = (perimeter, solutions)
        triangles.append((perimeter, solutions))

print(highest)

end = time.time()
print('execution time: ', end-start)
