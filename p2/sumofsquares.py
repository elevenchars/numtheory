import itertools
# import primefac
import sympy

nums = list(range(0, 41))

for i in range(1, 41):
    # print(nums[:i])
    # print(i)
    # print(f"n = {i}")
    pairs = itertools.combinations_with_replacement(nums[:i], 2)
    valid = []
    for pair in pairs:
        if pair[0] ** 2 + pair[1] ** 2 == i:
            valid.append(pair)
    # print(valid)
    if(valid):
        print(f"n = {i},\tf(n)={len(valid)}\t| {valid}")
        print(list(sympy.primefactors(i)))