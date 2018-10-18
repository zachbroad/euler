import math


nums = list(range(1, 101))

sum = 0
square = 0
for number in nums:
    sum += math.pow(number, 2)
    square += number

square = square*square
print('Difference: ', square-sum)
