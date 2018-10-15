

def is_palindrome(value):
    value = str(value)
    if value == value[::-1]:
        return True
    else:
        return False


def is_base2_palindrome(value):
    value = bin(value)
    return is_palindrome(str(value)[2:])


sum = 0
for i in range(1000000):
    if is_palindrome(i) and is_base2_palindrome(i):
        sum += i


print('Sum: ', sum)
