from sympy.ntheory import factorint
from sympy.ntheory import isprime
from math import gcd

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
    print(gcd(e,phi))
    if gcd(e, phi) != 1:
        raise Exception(f"e = {e} is not relatively prime to phi(N)")
    d = modinv(e, phi)
    M = pow(C, d, N)
    return M

def decrypt_rsa_single_prime(e, N, C):
    if not isprime(N):
        raise ValueError("N has to be prime")
    phi = N-1
    d = modinv(e, phi)
    M = pow(C, d, N)
    return M

#Part a

e = 17
N = 38210080753993935337519
C = 29202530725918700842079
M = decrypt_rsa(e, N, C)
print("The secret number M is: ",M)

#Part b

'''
e = 3
N = 237586812181653994808797835837127641
C = 14621362594515611576696983236378624
M = decrypt_rsa(e, N, C)
print("The secret number M is: ", M)
'''

#Part c

e = 65537
N = 782411451307002751974547518481
C = 750555647839236294597477460513
M = decrypt_rsa_single_prime(e, N, C)
print("The secret number M is: ", M)