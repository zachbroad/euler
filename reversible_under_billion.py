

import math

BILLION = 10**9

def get_sum(value):
	n = int(value)
	rn = int(str(value)[::-1])
	sum = n + rn
	# print('{} + {} = {}'.format(n, rn, sum))
	return int(sum)


def is_reversible(value):
	digits = list(str(value))

	for digit in digits:
		if int(digit) in [2,4,6,8]:
			return False

	if value < 101:
		return False

	if digits == digits[::-1]:
		return True

	return False

	# digits = list(str(value))
	# half = math.floor(len(digits) / 2)
	# if digits[:half] == digits[:-half]:
	# 	print('reverisble: ', value)
	# 	return True

	# return False

def compute():
	reversible_number_count = 0
	reversible = []
	batch = 1000
	for i in range(1, batch+1):
		sum = get_sum(i)
		if is_reversible(sum):
			reversible.append(i)
			reversible_number_count += 1


	print(reversible_number_count)
	reversible_number_count = len(reversible)
	print(reversible)

	print('Total: [{}] - Reversible: [{}]'.format(batch, reversible_number_count))
	print(reversible_number_count)



import time
start = time.time()
compute()
end = time.time()
print('Finished in {} seconds'.format(end-start))

# print(is_reversible(36))
# print(is_reversible(37))

# compute()