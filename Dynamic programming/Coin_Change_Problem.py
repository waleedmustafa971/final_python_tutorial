# The Coin Change Problem is a classic problem where, given an unlimited supply of coins of different denominations and a total amount, you have to find the minimum number of coins required to make up that amount.

# Problem Statement:
# You have n denominations of coins.
# You need to find the minimum number of coins needed to make a total amount amount.
# Dynamic Programming Approach:
# Define Subproblem: Let dp[x] represent the minimum number of coins needed to make amount x.
# Recurrence Relation:
# For each coin denomination coin, update the minimum number of coins for all amounts x: dp[x] = min(dp[x], dp[x-coin] + 1).
# Initialization: dp[0] = 0 because zero coins are needed to make amount 0.
# Final Answer: The final result will be in dp[amount].
# Here's the Python implementation:


import sys

def coin_change(coins, amount):
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0

    # Build the dp table
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != sys.maxsize else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print("Minimum coins required:", coin_change(coins, amount))
