

i = 0
fib = [1, 2]
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

even = [x for x in fib if x % 2 == 0]

sum = 0
for num in even:
    sum += num

print(sum)
