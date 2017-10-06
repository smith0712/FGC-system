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

B=1
C=1
while(True):
    a = p(C)
    b = p(B)
    v=a*b
    print(v)
    
    C=C+1
    B=B+1
    

 
       


