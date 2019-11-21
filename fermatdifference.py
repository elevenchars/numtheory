import math


def fd(n: int) -> tuple:
    """Calculate nontrivial factors of n using the fermat difference of
    squares method. This method works best when the factors p,q are near sqrt 
    n.

    There are more optimizations to be made, namely the sieve method described
    in the wikipedia page for this method.

    Arguments:
        n {int} -- number to factor

    Returns:
        tuple -- (p,q)
    """

    # lower bound for a
    a = math.ceil(math.sqrt(n))
    
    # a must be odd if n cong 1 (mod 4)
    if n % 4 == 1:
        if a % 2 == 0:
            a += 1
    else: # a must be even if n cong -1 (mod 4)
        if a % 2 == 1:
            a += 1

    # recall that n = a^2 - b^2
    b = math.sqrt(a**2 - n)

    while not b.is_integer():
        print(a, int(b))
        a += 2
        b = math.sqrt(a**2 - n)

    print("a,b found!")
    print(f"a = {a}")
    print(f"b = {int(b)}")
    return (int(a+b), int(a-b))


if __name__ == "__main__":
    n = int(input("Integer to factorize: "))
    p, q = fd(n)
    assert p*q == n
    print(f"p = {p}")
    print(f"q = {q}")
