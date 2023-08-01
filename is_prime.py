def Sieve(N):
    prime = [True for i in range(N+1)]
    p = 2
    arr=[]
    while (p * p <= N):
        if (prime[p] == True):
 
            for i in range(p * p, N+1, p):
                prime[i] = False
        p += 1
    for p in range(2, N+1):
        if prime[p]:
            arr.append(p)
    return arr
n=100000
m=Sieve(n)
arr2=[];
for i in range(len(m)+2):
    if m[i+1]-m[i]==2:
        arr2.append(m[i])
        arr2.append(m[i+1])
   
while (True):
    for i in  arr2:
        try:
            k=int(input())
            print(f"({m[k]}, {m[k+1]})")
        
        except EOFError:
            break
    
   
        
        
            
                
            
      