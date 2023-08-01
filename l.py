import math

def is_prime(n):
  
    for i in range(2, int(math.sqrt(n))+1, 2):
          
            if n % i == 0:
                return n,"is COMPOSITE TT"
            
    return n, "is PRIME!!"
while(True):
    m=int(input())
    if m==-1:
        break;
    else:
        out=is_prime(m)
        print(out)
        
    