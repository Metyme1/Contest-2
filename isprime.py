# import math

# def is_prime(n):
#     if n < 2:
#         return False
        
#     elif n == 2 or n == 3:
#         return True
#     elif n % 2 == 0:
#         return False
    
#     for i in range(3, int(math.sqrt(n))+1, 2):
#             if n % i == 0:
#                 return (n,"is composite TT")
#     return(n,"is prime!!")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    m = int(input())
    if m == -1:
        break
    elif is_prime(m):
        print("1")
    else:
        print("0")