from sympy.ntheory import factorint

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

'''
def factorize(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= 1
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
'''
def decrypt_rsa(e, N, C):
    factors = factorint(N)
    if len(factors) != 2:
        raise ValueError("N needs to be a product of two distinct primes")
    p,q = factors
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    M = pow(C, d, N)
    return M

e = 17
N = 38210080753993935337519
C = 29202530725918700842079
M = decrypt_rsa(e, N, C)
print("The secret number M is: ",M)