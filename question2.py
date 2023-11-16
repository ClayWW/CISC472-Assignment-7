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
    
def recover_rsa_sig(h_prime, s_bob_prime, e, N, append_length):
    h_prime =  int(h_prime, 16)
    s_bob_prime = int(s_bob_prime, 16)
    e = int(e, 16)
    N = int(N, 16)

    k = append_length * 4
    H = h_prime >> k
    s_bob = (s_bob_prime * modinv(16 ** (k*e), N)) % N
    s_bob_hex = hex(s_bob)
    H_hex = hex(H)

    return H_hex, s_bob_hex

h_prime = "0x9a4636438e6bd94b0103c26d9973680e00000"
s_bob_prime = "0x3d99849cce273e20ce5fa8785a29f0bf458b8cfb"
e = "0x5"
N = "0x68ef91088c021e0fcad6e4b1a8d0c2185182f903"
append_length = 5

H, s_bob = recover_rsa_sig(h_prime, s_bob_prime, e, N, append_length)
print("Original Hash (H):", H)
print("Bob's Signature on H:", s_bob)

