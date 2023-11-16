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

    factor = pow(16, k * e, N)

    mod_inv_factor = modinv(factor, N)
    s_bob = (s_bob_prime * mod_inv_factor) % N

    print("H_prime:", hex(h_prime))
    print("S_bob_prime:", hex(s_bob_prime))
    #print("Modular Inverse:", hex(mod_inv))
    print("Recovered H:", hex(H))
    print("Recovered Signature:", hex(s_bob))

    return hex(H), hex(s_bob)

def verify_sig(H, s_bob, e, N):
    H = int(H, 16)
    s_bob = int(s_bob, 16)
    e = int(e, 16)
    N = int(N, 16)

    compute_H = pow(s_bob, e, N)
    print("Computed H from Signature:", hex(compute_H))
    return compute_H == H

h_prime = "0x9a4636438e6bd94b0103c26d9973680e00000"
s_bob_prime = "0x3d99849cce273e20ce5fa8785a29f0bf458b8cfb"
e = "0x5"
N = "0x68ef91088c021e0fcad6e4b1a8d0c2185182f903"
append_length = 5

H, s_bob = recover_rsa_sig(h_prime, s_bob_prime, e, N, append_length)
print("Original Hash (H):", H)
print("Bob's Signature on H:", s_bob)

is_valid = verify_sig(H, s_bob, e, N)
print("Is the signature valid?", is_valid)


