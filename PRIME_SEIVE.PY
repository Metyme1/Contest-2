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
    return len(arr)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


    

a,b=(map(int,input().split()))
print(Sieve(a))
i=0
while(i<b):
    n=int(input())
    if is_prime(n):
        print("1")
    else:
        print("0")
    
    i+=1
    
    
    