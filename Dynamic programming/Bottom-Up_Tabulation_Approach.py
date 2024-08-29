def fibonacci_tabulation(n):
    # Base cases
    if n <= 1:
        return n

    # Create a table to store results of subproblems
    dp = [0] * (n + 1)
    dp[1] = 1

    # Fill the table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage
n = 10
print(f"Fibonacci({n}) =", fibonacci_tabulation(n))


# In both implementations, we are significantly improving the performance by storing previously computed values. The time complexity for both approaches is O(n), and the space complexity is also O(n) (or O(1) for optimized space in the iterative approach).