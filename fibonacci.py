def fibonacci(n):
    seq = [1,1]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 1:
        seq.append(fibonacci(n-1) + fibonacci(n-2))
        return seq
    
print(fibonacci(3))