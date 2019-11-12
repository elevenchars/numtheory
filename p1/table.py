from p1 import *

# this program prints a copy of the table.

print(" n | sn |sin | pn |pin")
for i in range(0, 43):
    print(f"{i :>2} | {s(i) :>2} | {si(i): >2} | {p(i) :> 2} | {pi(i) :> 2}")
