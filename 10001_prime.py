


primes = [2,3,5,7]
base_primes = [2, 3, 5, 7]
count = 9


import time
import math


start = time.time()


def is_prime(n):
	if n & 1 == 0:
		return 2

	d = 3
	while d * d <= n:
		if n % d == 0:
			return d

		d = d + 2


	return 0


while len(primes) < 10001:
	if is_prime(count) == 0:
		primes.append(count)

	count += 2

print(primes[-1], len(primes))
end = time.time()
print('exec time: ', end-start)
