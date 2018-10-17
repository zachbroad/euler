


def is_increasing(value):
	last = 0
	for char in str(value):
		if int(char) >= last:
			last = int(char)
		else:
			return False

	return True



def is_decreasing(value):
	last = int(str(value)[0])
	for char in str(value):
		if int(char) <= last:
			last = int(char)
		else:
			return False

	return True



def compute():
	import time

	start = time.time()
	total = 1
	increasing_numbers = 0
	decreasing_numbers = 0
	bouncy_numbers = 0

	computing = True

	while computing:
		if is_increasing(total):
			increasing_numbers += 1
		elif is_decreasing(total):
			decreasing_numbers += 1
		else:
			bouncy_numbers += 1

		if bouncy_numbers / total >= .99:
			print('SOLUTION FOUND: ', total)
			computing = False


		total += 1

	end = time.time()
	print('Increasing Numbers: ', increasing_numbers)
	print('Decreasing Numbers: ', decreasing_numbers)
	print('Bouncy Numbers: ', bouncy_numbers)
	print('bouncy/total: ', bouncy_numbers / total)
	print('Execution time: ', end-start)


		# increasing = is_increasing(i)
		# decreasing = is_decreasing(i)
		# bouncy = True if (!increasing && !decreasing) else False






compute()

