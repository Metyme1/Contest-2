def goldbach_conjecture(n):
   
    
    primes = [True]* (n+1)
    p = 2
    while (p * p <= n):
       
        if primes[p] == True:
            
            for i in range(p * 2, n+1, p):
                primes[i] = False
        p += 1
    min_diff = n
    for p in range(2, n+1):
        if primes[p]:
            if primes[n-p]:
                if abs(p - (n-p)) < min_diff:
                    min_diff = abs(p - (n-p))
                    a, b = p, n-p
    print(a, b)


while True:
    n = int(input())
    
    if(n == -1):
        break
    goldbach_conjecture(n)
    
    
    