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


def sum_primes(n):
    sum = 0
    for i in range(2, n):    
        if is_prime(i) == True:
            sum += i
    return sum
