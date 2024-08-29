# The Fibonacci sequence is defined as:

# Fib(0) = 0
# Fib(1) = 1
# Fib(n) = Fib(n-1) + Fib(n-2) for n >= 2
# A naive recursive solution will have a time complexity of O(2^n), which is inefficient for large n. We can optimize this using dynamic programming.

# Top-Down (Memoization) Approach


def fibonacci_memo(n, memo={}):
    # Base cases
    if n <= 1:
        return n
    
    # Check if result is already computed
    if n not in memo:
        # Recursively compute the Fibonacci number
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    
    return memo[n]

# Example usage
n = 10
print(f"Fibonacci({n}) =", fibonacci_memo(n))
