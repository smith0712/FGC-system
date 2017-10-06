def A():
          global d, n
          n=int(input('소인수분해할 자연수는?'))
          d = 2
         
          while d <= n: 
                if n%d == 0:
                           print(d)
                           n = n/d  
                else:
                       d = d +1
while True:
           A()
 
