from utils import *

if __name__ == "__main__":
    print(find_factorial(6))
    print(gcd(56, 98))
    print(is_prime(121))

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1
