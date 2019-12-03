from fermatdifference import *
import math


def triples(n: int) -> list:
    """Generate a (non-exhaustive) list of primitive pythag triples.

    Arguments:
        n {int} -- number of triples to generate

    Returns:
        list -- list [(a, b, c), ...]
    """
    trips = []
    i = 3
    while len(trips) < n:
        print(i)
        res = fd(i)
        if res:
            a, b, _, __ = res
            if math.gcd(a, b) != 1 or b == 0:
                i += 1
                continue
            trips.append((i, 2*a*b, a ** 2 + b ** 2))
            i += 1
        else:
            i += 1
            continue
    return trips


if __name__ == "__main__":
    n = int(input("Number of triples to generate: "))
    trips = triples(n)
    trips = sorted(trips, key=lambda x: x[2])
    for triple in trips:
        print(triple)
