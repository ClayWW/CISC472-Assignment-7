from Crypto.Util.number import inverse, getPrime

def gen_keypair(size):
    """
    Generates a pair of keys for Paillier encryption.
    
    Parameters:
    size (int): Bit size of the prime numbers to be generated.

    Returns:
    tuple: The public key (N, g) and private key (phi, mod_inverse).
    """
    p = getPrime(size)  # Get a prime number
    q = getPrime(size)  # Get another prime number
    N = p * q  # The modulus
    g = N + 1  # g is set as N+1 in Paillier
    phi = (p - 1) * (q - 1)  # Euler's totient function
    mod_inverse = inverse(phi, N)  # Modular inverse of phi modulo N
    return (N, g), (phi, mod_inverse)

def paillier_encrypt(M, R, key):
    """
    Encrypts a message using Paillier.

    Parameters:
    M (int): The message to be encrypted.
    R (int): A random number.
    key (tuple): The public key (N, g).

    Returns:
    int: The encrypted message.
    """
    N, g = key
    # Paillier encryption formula
    return (pow(g, M, N**2) * pow(R, N, N**2)) % (N**2)

def paillier_decrypt(C, p_key):
    """
    Decrypts a message encrypted using Paillier.

    Parameters:
    C (int): The ciphertext to be decrypted.
    p_key (tuple): The private key (N, phi, mod_inverse).

    Returns:
    int: The decrypted message.
    """
    N, phi, mod_inverse = p_key
    d = pow(C, phi, N**2) 
    e = (d - 1) // N 
    return (e * mod_inverse) % N  

# Test case 3b
C = 2408522148575687340805180772
N_squared = 7905547463165041131990033721
N = int(N_squared**0.5)
p = q = int(N**0.5)
phi = (p-1)*(q-1)
mod_inverse = inverse(phi, N)
p_key = (N, phi, mod_inverse)
M_decrypted = paillier_decrypt(C, p_key)
print("Decrypted M: ", M_decrypted)

# Test case 3c
C1 = 2726070680403153614394063339
C2 = 5866866636167850787431170831
C3 = (C1 * C2) % N_squared
print("Ciphertext of M3: ", C3)
