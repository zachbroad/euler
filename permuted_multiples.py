
def get_digits(value):
    value = str(value)
    print(sorted(value))
    return sorted(value)


i = 1
running = True
while running:
    digits = get_digits(i)
    valid = True
    for j in range(1, 7):
        if digits != get_digits(i*j):
            valid = False
    if valid:
        print('SOLUTION: ', i)
        running = False
    i += 1
