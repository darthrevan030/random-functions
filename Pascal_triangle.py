def factorial(n):
    num_list = list(range(1, n+1))
    product = 1
    for i in num_list:
      product = product * i
    return product

def binomial(n):
    coeff = []
    for i in range(n+1):
        a = factorial(n) // (factorial(i) * factorial(n-i))
        coeff.append(a)
    return coeff


def print_pascal_triangle(n):
    list_of_tiers = []
    for i in range(0, n+1):
        b = binomial(i)
        list_of_tiers.append(b)
    for j in list_of_tiers:
        for x in j:
            print(x, end = " ")
        print()
    
print_pascal_triangle(30)