# define prime function
def is_prime(num):
    if (num < 2): return False
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True

# list comprehension
primes = [ num for num in range(100) if is_prime(num) ]

# unpack and print
print(*primes)
