# The 0/1 Knapsack Problem is a classic problem in combinatorial optimization. Given a set of items, each with a weight and value, determine the maximum value that can be obtained by selecting a subset of the items such that their total weight doesn't exceed a given capacity. Each item can either be included (1) or excluded (0) from the knapsack.

# Problem Statement:
# You have n items, each with a weight w[i] and a value v[i].
# You have a knapsack with a capacity W.
# Your goal is to maximize the total value without exceeding the capacity.
# Dynamic Programming Approach:
# Define Subproblem: Let dp[i][j] represent the maximum value achievable with the first i items and a knapsack capacity of j.

# Recurrence Relation:
# If the ith item is not included: dp[i][j] = dp[i-1][j].
# If the ith item is included: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i]).
# Initialization: dp[0][j] = 0 for all j, because no items means zero value.
# Final Answer: The final result will be in dp[n][W], which represents the maximum value with all n items and capacity W.
# Here's the Python implementation:

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option to include the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Can't include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum value in Knapsack:", knapsack(values, weights, capacity))
