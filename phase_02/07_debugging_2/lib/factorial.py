def factorial_solved(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

def factorial_original(n):
    product = 1
    while n > 0:
        # The error is that we are modifiying the value of n before making the operation
        # which will instead of ending up at 1 as it should, it will end up on 0. 0 * x = 0
        n -= 1
        product *= n
    return product

print(factorial_solved(5))
print(factorial_original(5))

# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 0