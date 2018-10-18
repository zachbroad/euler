from decimal import *


def recurring_digits(value):
    digits = str(value).split('.')[1]
    print(digits)
    cycle = []
    for digit in digits:
        cycle.append(digit)
        for k, v in enumerate(cycle):
            try:
                if v == digits[k] and v == digits[k+len(cycle)]:
                    return True
                else:
                    return False
            except:
                return False

    return True


def compute():
    for i in range(2, 1000+1):
        n = recurring_digits(Decimal(1.0) / Decimal(i))
        print(n)


# compute()

print(recurring_digits(1.0/7))
