def Sieve(N):
    arr=[]
    prime  = [True] * (N+1)
    p = 2
    while (p * p <= N):
        if (prime[p] == True):
 
            for i in range(p * p, N+1, p):
                prime[i] = False
        p += 1
    for p in range(2, N+1):
        if prime[p]:
            arr.append(p)
    print(sum(arr))
num=int(input())
Sieve(num)



