import math
def factor(n):
    arr=[]
    is_prime=[True]*(n+1)
    for i in range(1,int(math.sqrt(n)+1)):
        if is_prime[i]:
            
            for j in range(i*i,n+1,i):
                is_prime[j]=False
        for i in range(2,n+1):
            if is_prime[i] and n%i==0:
                arr.append(i)
        return arr

t=int(input())
for case in range(1,t+1):
    n=int(input())
    out=factor(n)
    print(f"Case {case}: {' '.join(map(str, out))}")