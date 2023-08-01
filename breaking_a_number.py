import math

def factors(num):
    arr = []
    prime = [True] * (num+1)
    for i in range(2, int(math.sqrt(num))+1):
        if prime[i]:
            for j in range(i*i, num+1, i):
                prime[j] = False
    
   
    for i in range(2, num+1):
        if prime[i] and num % i == 0:
            k+=1
            arr.append(i)
    
    return arr

while(True):
    m=int(input())
    if m==-1:
       break
    else:
        out=factors(m)
        print(out)
    