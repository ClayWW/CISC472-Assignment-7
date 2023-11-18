from sympy.ntheory import isprime
import math

def decrypt_rsa_single_prime(e, N, C):
    """
    Decrypts a ciphertext for a special kind of RSA where the modulus is a prime number squared.
    
    Parameters:
    e (int): Public exponent in RSA.
    N (int): The RSA modulus, which is a prime squared.
    C (int): The encrypted message.

    Returns:
    int: The original message before it was encrypted.
    """
    #Find the prime number that when squared gives N
    p = math.isqrt(N)
    if not isprime(p):
        raise ValueError("N should be a square of a prime number")
    #Figure out the private key and use it to decrypt C
    d = pow(e, -1, (p-1)**2)
    return pow(C, d, N)

def eth_root(C, e):
    """
    Gets the e-th root of C, mainly for when you're dealing with RSA and small e values.
    It's finding what number was raised to the e-th power to get C.

    Parameters:
    C (int): The number you're finding the root of.
    e (int): Which root you're trying to find (like square root, cube root, etc.).

    Returns:
    int: The e-th root of C.
    """
    #Start looking for the e-th root using a range-finding method
    high, low = 1, 0
    while high ** e <= C:
        high *= 2
    low = high // 2

    #Narrow down to the exact or closest number to the e-th root
    while low < high:
        mid = (low + high) // 2
        if mid ** e < C:
            low = mid + 1
        else:
            high = mid
    return low if low ** e == C else low - 1

# Test cases
e = 17
N = 38210080753993935337519
C = 29202530725918700842079
M = eth_root(C, e)
print("The secret number M is: ", M)

e = 3
N = 237586812181653994808797835837127641
C = 14621362594515611576696983236378624
M_b = eth_root(C, e)
print("The secret number M is: ", M_b)

e = 65537
N = 782411451307002751974547518481
C = 750555647839236294597477460513
M = decrypt_rsa_single_prime(e, N, C)
print("The secret number M is: ", M)
