def iterative_factorial(n):

    result = 1

    while n>1:

        result = result * n

        n = n - 1

    return result

print(iterative_factorial(0))
print(iterative_factorial(1))
print(iterative_factorial(5))

def recursive_factorial(n):

    if (n == 1) | (n == 0):
        return 1
    else:
        return n * recursive_factorial(n-1)


print(recursive_factorial(0))
print(iterative_factorial(1))
print(recursive_factorial(5))