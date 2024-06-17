def factorial(n: int) -> int:
    if n<=1:
        return 1 # This is our base case
    return n*factorial(n-1) # This is our recursive step

print(factorial(5))