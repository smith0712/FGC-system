import hashlib
T=""
G=""
V=0
Q=1

plaintext =''
ciphertext=''
pad=''

key ='FGCsystem1234567890'

def p(a):
    if(a==1):return 2
    if(a==2):return 3
    c=0
    n=3
    z=1
    b=0

    a=a-2
    while b<a:
        while True:
            n =n+2
            c=2
            z=1
            while c<=n**(0.5):
                if(n%c ==0):
                    z=0
                    break
                c=c+1
            if(z==1):break
        b=b+1
    return n

def decrypt():
    # decrypt
    plaintext = ''
    for i in range(32):
        plaintext += chr(ord(pad[i])^ord(ciphertext[i]))
    print(plaintext)
a=p(C)
b=p(B)
V=a*b

data =open('X.txt')
data.read().split()
v=data


if(V%(2**Q-1)==0):
    V/(2**Q-1)=w
    2**Q-1=m
    key = str(a)
    plaintext=T+'0'+G+'0'+str(V)+'0'+str(m)+'0'+str(w)
    pad = str(hashlib.sha256(key.encode('utf-8'))
    for f in range(len(plaintext)):
              
        ciphertext += chr(ord(pad[f])^ord(plaintext[f]))
        if (v==ciphertext):
              print("miner gets 5 FGC")
        else:
              print("fail to get Four glasses coin")
                          
              
    
else:
    Q=Q+1

