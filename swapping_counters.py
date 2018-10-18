def make_row(n=3):
    row = [0] * ((2 * n) + 1)
    i = 0
    while i < n:
        row[i] = -1
        row[-i - 1] = 1
        i += 1

    return row


def swap(row, start, end):
    start = row[start]
    end = row[end]
    row[start] = end
    row[end] = start
    return row


def solve(row):
    solution = list(reversed(row))

    mod = 1
    moves = 0
    unsolved = True
    while unsolved:
        for index, block in enumerate(row):
            # move right

            # attempt to move to the right
            # if not, check next
            # if we can move, swap the positions

            # move left

            try:
                if row[index + mod] == 0:
                    row[index], row[index + mod] = row[index + mod], row[index]
                    moves += 1
                elif row[index + (mod * 2)] == 0 and row[index + mod] == -block:
                    row[index], row[index + (mod * 2)] = row[index + (mod * 2)], row[index]
                    moves += 1
            except IndexError:
                mod = -mod

            print('[{}]: {}'.format(moves, row))

            if row == solution:
                unsolved = True
                print('solution: ', row)
                print('{} moves'.format(moves))
                return
        # switch directions


print(solve(make_row(3)))


def can_slide(row, start, end):
    pass
