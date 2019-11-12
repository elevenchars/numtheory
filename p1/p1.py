# return the absolute least residue congruent to x (mod m)
def absres(x, m):
    r = x % m
    if r > m//2:
        return r - m
    else:
        return r


def gcd(a, b):
    # edge cases
    assert a != 0 or b != 0
    if b == 0:
        return a

    r = a % b
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a - b * q

    return b


# return a list of the invertible integers mod n.
def invertibles(n):
    c = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            c.append(i)
    return c


# sum of all elements mod n
def s(n):
    if n == 0:
        return 0
    sum = 0
    for i in range(0, n):
        sum += i
    return absres(sum, n)


# sum of all invertible elements mod n
def si(n):
    if n == 0:
        return 0
    sum = 0
    for i in invertibles(n):
        sum += i
    print(sum)
    return absres(sum, n)


# product of all elements mod n
def p(n):
    return 0


# product of all invertible elements mod n
def pi(n):
    if n == 0:
        return -1
    prod = 1
    for i in invertibles(n):
        prod *= i
    return absres(prod, n)
