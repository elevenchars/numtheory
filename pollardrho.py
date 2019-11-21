import math
import random

def rho(n: int) -> int:
    """Naive implementation of Pollard's rho algorithm from
    https://www.cs.colorado.edu/~srirams/courses/csci2824-spr14/pollardsRho.html
    Generate a nontrivial factor of n.
    This will fail! It sucks!
    
    Arguments:
        n {int} -- number to factor
    
    Returns:
        int -- Nontrivial factor of n
    """
    a = random.randint(0,n-1)
    f = lambda x: (x**2 + a) % n
    x = 2 # starting value
    y = 2
    while True:
        x = f(x)
        y = f(f(x))
        d = math.gcd(abs(y-x), n)
        print(x,y,d)
        if d > 1:
            return d
        if x == y:
            print("cycle, retry")
            return rho(n) # big brain


print(rho(1821089))
print("\a")