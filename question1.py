from sympy.ntheory import factorint
from sympy.ntheory import isprime
import math
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def decrypt_rsa(e, N, C):
    factors = factorint(N)
    if len(factors) != 2:
        raise ValueError("N needs to be a product of two distinct primes")
    p,q = factors
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both factors need to be prime")
    if p*q != N:
        raise ValueError("The product of the factors does not equal N")
    phi = (p-1)*(q-1)
    print("Phi: ", phi)
    print(math.gcd(e,phi))
    if math.gcd(e, phi) != 1:
        raise Exception(f"e = {e} is not relatively prime to phi(N)")
    d = modinv(e, phi)
    M = pow(C, d, N)
    return M

def decrypt_rsa_single_prime(e, N, C):
    p = math.isqrt(N)
    if not isprime(p):
        raise ValueError("The square root of N is not prime, invalid N given assumptions")
    phi = (p-1)**2
    d = pow(e, -1, phi)
    M = pow(C, d, N)
    return M

def eth_root(C, e):
    high = 1
    while high ** e <= C:
        high *= 2
    low = high//2

    while low < high:
        mid = (low + high) // 2
        if mid ** e < C:
            low = mid+1
        else:
            high = mid
    return low if low ** e == C else low-1

#Part a

e = 17
N = 38210080753993935337519
C = 29202530725918700842079
'''
M = decrypt_rsa(e, N, C)
print("The secret number M is: ",M)
'''
M = eth_root(C, e)
print("The secret number M is: ",M)

#Part b


e = 3
N = 237586812181653994808797835837127641
C = 14621362594515611576696983236378624
'''
M = decrypt_rsa(e, N, C)
print("The secret number M is: ", M)
'''

M_b = eth_root(C, e)
print("The secret number M is: ", M_b)

#Part c

e = 65537
N = 782411451307002751974547518481
C = 750555647839236294597477460513
M = decrypt_rsa_single_prime(e, N, C)
print("The secret number M is: ", M)