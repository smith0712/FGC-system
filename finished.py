v=0

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
C=2
while(True):
    a = p(C)
    b = p(B)

    v=a*b #v 값은 소수
    print(v)
    def A():
          global d, n
          n= v
          d = 2
         
          while d <= n: 
                if n%d == 0:
                           print(d)
                           n = n/d  
                else:
                       d = d +1
   
    A() 
    C=C+1
    B=B+1
    

 
 
   


