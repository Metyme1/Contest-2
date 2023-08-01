# def prime(n):
#     arr = []
#     primes = []
    
#     for i in range(2, n+1):
#         if i not in arr:
#             primes.append(i)
            
                
#             for j in range(i*i, n+1, i):
#                 arr.append(j)
#     return primes

# n = int(input())
# m=prime(n)
# print(m[6])

def Sieve(N):
    prime = [True for i in range(N+1)]
    p = 2
    while (p * p <= N):
        if (prime[p] == True):
 
            for i in range(p * p, N+1, p):
                prime[i] = False
        p += 1
    for p in range(2, N+1):
        if prime[p]:
            print(p, end="")
num=int(input())
Sieve(num)











