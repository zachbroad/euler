from itertools import cycle
from operator import xor


# read file


def read_cipher_data():
    # Reads cipher data from txt file and returns a list

    data = []

    with open('p059_cipher.txt') as f:
        data = f.readline().split(',')

    return data


def decrypt(data, key):
    # XOR decryption

    de = []

    de = ''.join(chr(xor(int(n), k)) for (n, k) in zip(data, cycle(key)))

    return de


def save(results):
    with open('cipher_results.txt', 'w+') as f:
        for k, r in results.items():
            # convert to string

            f.write('[{}]'.format(k))
            f.write('\n')
            f.write(r)
            f.write('\n')
            f.write('\n')


# 97-122

def tryall():
    data = read_cipher_data()
    results = {}

    key = ''

    for i in range(97, 122 + 1):
        for j in range(97, 122 + 1):
            for k in range(97, 122 + 1):
                key = [i, j, k]
                keyStr = '{}{}{}'.format(chr(i), chr(j), chr(k))

                results[keyStr] = (decrypt(data, key))

    print('Saving resutls...')
    save(results)


'''
# SOLUTION :
# exp
[exp]
An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
'''


def find_sum():
    sum = 0
    data = []
    with open('xor_solution.txt') as f:
        data = f.readline().rstrip()



    for d in data:
        print(ord(d))
        sum += ord(d)

    print(sum) # 129448


if __name__ == '__main__':
    # tryall()
    find_sum()
