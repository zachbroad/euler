

def pandigital(seed, factor):
    concatenated_product = ''
    for i in range(1, factor+1):
        concatenated_product += str(seed*i)

    return int(concatenated_product)


def valid(pandigital):
    p = list(str(pandigital))

    if len(p) != 9:
        return False

    for i in range(1, 9+1):
        if str(i) not in p:
            return False

    return True


# factors
f1 = 1
f2 = 1

pandigitals = []


def compute():
    highest = 0
    hitten = False
    while not hitten:
        for f1 in range(1, 10000):
            for f2 in range(1, 20):
                pd = pandigital(f1, f2)
                if valid(pd):
                    pandigitals.append(pd)

                if pd <= 999999999 and valid(pd):
                    pandigitals.append(pd)
                    highest = pd if pd > highest else highest

                if pd > 999999999:
                    hitten = True

    print(pandigitals[-1])


import time
start = time.time()
compute()
end = time.time()
print(end-start, ' seconds')
