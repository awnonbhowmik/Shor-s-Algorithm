from math import gcd
from random import randint

def period(x,N):
  r = -1
  for r in range(N):
    if pow(x,r,N)==1:
      return r
"""this can be used to do prime factoring of a composite number, for that
we will just go back to the basics, implement a bool isprime(n) function
and while not prime found, keep running shors_breaker(N)

However, in the case of public key cryptography, N = pq and no further
calculations are required"""
def shors_breaker(N):
    N = int(N)
    while True:
        a=randint(0,N-1)
        g=gcd(a,N)
        if g!=1 or N==1:
            return g,N//g
        else:
            r=period(a,N) 
            if r % 2 != 0:
                continue
            elif pow(a,r//2,N)==-1:
                continue
            else:
                p=gcd(pow(a,r//2)+1,N)
                q=gcd(pow(a,r//2)-1,N)
                if p==N or q==N:
                    continue
                return p,q

N=int(input("Enter a number:"))
#Prevent trouble, making sure no edge cases are even executed in the function
assert N>0,"Input must be positive"
#now that we have a good value, run the function
print(shors_breaker(N));
