from values import ct, p, q, e
from math import lcm
from Crypto.Util.number import inverse, long_to_bytes

n = p*q
totient = lcm( (p-1), (q-1) )
d = inverse(e, totient)

flag = pow(ct, d, n)
flag = long_to_bytes(flag).decode()

print(flag)
