def allPrimeNumbersBetweenParameters(min, max):
    i = min
    primeNumbers = []
    while i <= max:
        if isPrime(i):
            primeNumbers.append(i)
            print("Added "+str(i))

        i += 1
    return primeNumbers

def isPrime(num):
    if num == 1:
        return True
    else:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(str(num) +" is not a prime.")
                return False
            i += 1
        else:
            print(str(num) +" is a prime number.")
            return True

