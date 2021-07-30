import random
import math

def gcd(a,b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    if(a == b):
        return a
    if(a>b):
        return gcd(a%b,b)
    return gcd(a,b%a)

def powmod(x,y,p):
    res = 1
    x = x % p
    while(y>0):
        if(y&1):
            res = (res*x)%p
        y = y>>1
        x = (x*x)%p
    return res

def encrypt(plain,e,n):
    cipher = []
    print("Hex value of encrypted data:",end="")
    for m in plain:
        c = powmod(ord(m),e,n)
        print(hex(c),end="")
        cipher.append(c)
    print("\n")
    return cipher
	
def decrypt(cipher,d,n):
    print("Decryption:",end="")
    for m in cipher:
        c = powmod(m,d,n)
        print(chr(c),end="")

def isPrime(n):
    for i in range(2,round(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

def getPrime():
    primes = []
    for n in range(100,5000):
        if(isPrime(n)):
            primes.append(n)
    return random.choice(primes)

def main():
    print("|--RSA--|")
    plain = str(input("Enter plaintext:"))
    p = getPrime()
    q = getPrime()
    while(p == q):
        q = getPrime()
    n = p*q
    totient = (p-1)*(q-1)
    while(True):
        e = random.randint(1,totient-1)
        if(gcd(totient,e) == 1):
            break
    for i in range(1,totient):
        if((i*e)%totient == 1):
            d = i
            break
    print("p = {}\nq = {}\nn = {}\ntotient = {}\ne(public key) = {}\nd(private key) = {}".format(p,q,n,totient,e,d))
    decrypt(encrypt(plain,e,n),d,n)
    print("\n---------------------------")
	
main()
input()
