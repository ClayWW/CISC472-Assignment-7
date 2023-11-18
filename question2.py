import sympy
#The code works but it just takes a long time to load

def priv_exponent(e, p, q):
    """
    Finds the private exponent for RSA.

    Parameters:
    e (int): The public exponent (a part of the public key).
    p (int): One of the prime factors of the RSA modulus.
    q (int): The other prime factor of the RSA modulus.

    Returns:
    int: The private exponent (the secret part of the key).
    """
    phi = (p-1)*(q-1)
    return sympy.mod_inverse(e, phi)

def verify_sig(h_prime, s_prime, d, N):
    """
    Checks if a signature is legit

    Parameters:
    h_prime (int): The hashed message, a bit altered.
    s_prime (int): The signature you want to check.
    d (int): The private exponent.
    N (int): The RSA modulus.

    """
    s_prime_check = pow(h_prime, d, N)
    assert s_prime == s_prime_check
    print("S' and calculated S' match")

def sign_m(H, d, N):
    """
    Signs a message

    Parameters:
    H (int): The original hashed message.
    d (int): The private exponent.
    N (int): The RSA modulus.

    Returns:
    int: The signature of the hashed message.
    """
    return pow(H, d, N)

def factor_mod(N):
    """
    Breaks down the RSA modulus into its prime factors. 

    Parameters:
    N (int): The RSA modulus.

    Returns:
    tuple: The two prime numbers that multiply to give the RSA modulus.
    """
    factors = sympy.factorint(N)
    primes = list(factors.keys())
    if len(primes) != 2:
        raise ValueError("N does not have exactly two prime factors")
    return primes[0], primes[1]


# Test case
H = int("0x9a4636438e6bd94b0103c26d9973680e", 16)
h_prime = int("0x9a4636438e6bd94b0103c26d9973680e00000", 16)
s_bob_prime = int("0x3d99849cce273e20ce5fa8785a29f0bf458b8cfb", 16)
N = int("0x68ef91088c021e0fcad6e4b1a8d0c2185182f903", 16)
e = 0x5

p, q = factor_mod(N)
d = priv_exponent(e, p, q)
verify_sig(h_prime, s_bob_prime, d, N)
s_bob = sign_m(H, d, N)
print("Signature on " + hex(H) + " : " + hex(s_bob))
