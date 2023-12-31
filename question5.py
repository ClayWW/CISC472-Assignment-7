from sympy import gcd

#Provided values
N = 26213517554099922793186935435728758051686512622843261831745610817301320968502179929690051737030060551716308920108899
X1 = 51289415566237296447077617272311907630200377878486597995739301812010542866350392331721490900734358271148517989552
Xp = 3027503849476280959823276181352805025641001341476507072667
Xq = 4550626887371805493029974545014553994625133406284787914537

#finding the difference between the faulty signaute and its components
difference_of_p = abs(X1 - Xp)
difference_of_q = abs(X1 - Xq)

#using gcd to find the factors of N based on the differences
p = gcd(N, difference_of_p)
q = gcd(N, difference_of_q)

#if p is 1, calculate it by dividing N by q
if p == 1:
    p = N // q

#print out factors
print("Factor p of N: ", p)
print("Factor q of N: ", q)

