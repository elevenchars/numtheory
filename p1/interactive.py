from p1 import *

# This program provides a way for me to interactively test values of m.

while True:
    inp = input("Enter a modulus m (e to exit): ")
    if inp.lower() == "e":
        exit(0)

    if not inp.isdigit():
        print("Please enter an integer.")
        continue

    m = int(inp)
    print("")
    print(f"Inverses (mod {m}):")
    print(invertibles(m))

    print(f"Sum of elements (mod {m})")
    print(s(m))

    print(f"Sum of invertible elements (mod {m})")
    print(si(m))

    print(f"Product of invertible elements (mod {m})")
    print(pi(m))
