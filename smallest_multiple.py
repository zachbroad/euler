import time

def smallest():
    count = 2520
    found = False
    while not found:
        valid = True
        for number in range(1,20):
            if count % number != 0:
                valid = False
                break

        if valid:
            return count
        else:
            print('not valid', count)

        count += 2520



start = time.time()
print('Found smallest: ', smallest())
end = time.time()
print('execution time: {} seconds'.format(end-start))
