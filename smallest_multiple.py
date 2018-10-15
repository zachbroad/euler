

def smallest():
    count = 1
    found = False
    while not found:
        valid = True
        for number in range(1, 20):
            if count % number != 0:
                valid = False
                break

        if valid:
            return count
        else:
            print('not valid', count)

        count += 10


print('Found smallest: ', smallest())
