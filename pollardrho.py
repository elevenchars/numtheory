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
    while(True): # Danger!
        y = f(x)
        d = math.gcd(abs(y-x), n)
        if d > 1:
            return d
        x = y


print(rho(625))