def is_prime(n):
    isPrime = False
    
    if n <= 1:
        isPrime = True
    
    x = 1 + (n**0.5)
    y = int(x)
    
    if n > 1:
        for i in range(2, y):
            if (n % i) == 0:
                isPrime = False
                break
        else:
            isPrime = True
    else:
        isPrime = False
    
    return isPrime


def printprimes(a,b):
    primes = []
    for i in range(a,b):    
        if is_prime(i) == True:
            primes.append(i)
    print(*primes, sep = ", ", end="")

printprimes(10000, 10050)
            
