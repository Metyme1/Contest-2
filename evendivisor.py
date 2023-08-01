def count_even_divisors(prime_factors):
    count = 1
    for p, a in prime_factors:
        if p == 2:
            count *= (a + 1)
        else:
            count *= (2*a + 1)
    return count

# Reading the input
t = int(input())
for _ in range(t):
    k = int(input())
    prime_factors = []
    for i in range(k):
        p, a = map(int, input().split())
        prime_factors.append((p, a))

    # Computing the number of even divisors
    result = count_even_divisors(prime_factors)

    # Printing the result
    print(result)