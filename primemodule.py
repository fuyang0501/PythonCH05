def isprime(n):
    # check whether n is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_primes(n):
    # prints all prime numbers less than n    
    for i in range(2, n):
        if isprime(i):
            print(i)



def get_primes(n):
    # returns a list of prime numbers less than n
    primes = []
    for i in range(2, n):
        if isprime(i):
            primes.append(i)
    return primes