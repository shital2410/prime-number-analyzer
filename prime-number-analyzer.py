import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes_in_range(start, end):
    prime_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


print("Is 7 prime?:", is_prime(7))
print("Is 0 prime?:", is_prime(0))
print("Primes between 1 and 50:", generate_primes_in_range(1, 50))
