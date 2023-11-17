'''
Part a

(N-1)^d ≅ N-1 mod N when d is a positive odd integer
d = 2k+1 (which is always odd)
(N-1)^d = (N-1)^(2k+1) = (N-1)^2k(N-1)
(N-1)^2k = Nq + 1 for some integer q
(N-1)^d = (Nq+1)(N-1)
(N-1)^d = N^(2)q - Nq + N -1 = N(Nq - q + 1) - 1
N(Nq - q + 1) -1 is of the form Np - 1 for some integer p
Congruence to -1 mod N, or N-1 mod N. Therefore,
(N-1)^d ≅ N-1 mod N


Part b

a|c and b|c therefore there exists two integers m and n such that c = am and c = bn
GCD(a,b) = 1, so can use Bezout identity
There exists two integers x and y such that ax + by = 1
Multiply by c to get c(ax + by) = c
acx + bcy = c
Substitute c = am and c = bn
am^2x + bn^2y = c
am^2x and bn^2y are both divisible by ab, sum must also be divisible by c
Therefore ab|c
'''