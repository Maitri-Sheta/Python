def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("Factorial of 5:", factorial(5))
print("Fibonacci of 7:", fibonacci(7))
print("GCD of 48 and 18:", gcd(48, 18))