import random
import hashlib

v=0
B=1
C=2

plaintext = ''
ciphertext = ''
pad = ''

key = 'FGCsystem1234567890'

def p(a):
    if(a == 1): return 2
    if(a == 2): return 3
    c=0
    n=3
    z=1
    b=0
    
    a = a-2
    while b<a:
        while True:
            n = n+2
            c=2
            z=1
            while c<=n**(0.5):
                if(n%c == 0):
                    z=0
                    break
                c = c + 1
            if(z == 1): break
        b = b + 1
    return n

"""def encrypt():
    # encrypt
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(ord(pad[i])^ord(plaintext[i]))"""


def decrypt():
    # decrypt
    plaintext = ''
    for i in range(32):
        plaintext += chr(ord(pad[i])^ord(ciphertext[i]))
    print(plaintext)

for i in range(50):
    
    a = p(C)
    b = p(B)
    v=a*b
    key = str(a)
    plaintext = str(v)
    pad = str(hashlib.sha256(key.encode('utf-8')).digest())
    for f in range(len(plaintext)):
        ciphertext += chr(ord(pad[f])^ord(plaintext[f]))
    
    print("block" + str(i) + "is added to the blockchain!\n" + "hash: " + ciphertext + "\n\n")
    
    C=C+random.randint(1,C)
    B=B+random.randint(1,B)
