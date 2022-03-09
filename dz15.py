

def is_prime(a):
    if a > 1:
        for i in range(2, int(a / 2) + 1):
            if (a % i) == 0:
                return False
            else:
                return True

    else:
        return False

def primes_interval(a, b):
    array_of_primes = []
    for i in range(a, b):
        if is_prime(i):
            array_of_primes.append(i)
    return array_of_primes

def dz15():
    primes_list = primes_interval(10, 100)
    squared_primes = list(map(lambda x: x * x, primes_list))
    print(primes_list)
    print(squared_primes)

if __name__ == '__main__':
    dz15()