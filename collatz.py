import time


def get_next(input):
    if input % 2 == 0:
        return input/2
    else:
        return (input * 3) + 1


def generate_sequence(seed):
    sequence = [seed]
    while sequence[-1] > 1:
        sequence.append(get_next(sequence[-1]))

    return sequence


def find_longest():
    longest = (0, 0)
    for i in range(1000000):
        seq = generate_sequence(i)
        if len(seq) > longest[1]:
            longest = (i, len(seq))

    print('Seed {} with length of {}'.format(longest[0], longest[1]))


start = time.time()
find_longest()
end = time.time()
print('Execution time: ', end-start)
