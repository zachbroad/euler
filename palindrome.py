

def is_palindrome(value):
    value = str(value)
    if value == value[::-1]:
        return True
    else:
        return False


def compute():
    fac1, fac2 = 999, 999
    largest = 0
    while fac1 > 99:
        fac2 = 999
        while fac2 > 99:
            product = fac1 * fac2
            if is_palindrome(product):
                largest = product if product > largest else largest
            fac2 -= 1

        fac1 -= 1

    print('Largest palindrome: ', largest)


compute()
