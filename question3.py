from Crypto.Util.number import inverse, getPrime

def gen_keypair(size):
    p = getPrime(size)
    q = getPrime(size)
    N = p*q
    g = N+1
    phi = (p-1)*(q-1)
    mod_inverse = inverse(phi, N)
    return (N, g), (phi, mod_inverse)

def paillier_encrypt(M, R, key):
    N, g = key
    return (pow(g, M, N**2) * pow(R, N, N**2)) % (N**2)

def paillier_decrypt(C, p_key):
    N, phi, mod_inverse = p_key
    d = pow(C, phi, N**2)
    e = (d-1)//N
    return (e*mod_inverse) % N

#3b

C = 2408522148575687340805180772
N_squared = 7905547463165041131990033721
N = int(N_squared**0.5)
p = q = int(N**0.5)
phi = (p-1)*(q-1)
mod_inverse = inverse(phi, N)
p_key = (N, phi, mod_inverse)
M_decrypted = paillier_decrypt(C, p_key)
print("Decrypted M: ",M_decrypted)

#3c
C1 = 2726070680403153614394063339
C2 = 5866866636167850787431170831
C3 = (C1 * C2) % N_squared
print("Ciphertext of M3: ", C3)


