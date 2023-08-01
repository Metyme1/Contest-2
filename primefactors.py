def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

while True:
    m = int(input())
    if m == -1:
        break
    else:
        factors_str = ' '.join(map(str, prime_factors(m)))
        print(factors_str)