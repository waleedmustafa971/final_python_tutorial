# The Longest Common Subsequence problem is about finding the longest subsequence that is common between two strings. A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Problem Statement:
# Given two strings, s1 and s2, find the length of their longest common subsequence.
# Dynamic Programming Approach:
# Define Subproblem: Let dp[i][j] represent the length of the longest common subsequence for the first i characters of s1 and the first j characters of s2.
# Recurrence Relation:
# If s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1.
# Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
# Initialization: dp[0][j] = 0 for all j and dp[i][0] = 0 for all i, because an empty string has no common subsequence.
# Final Answer: The final result will be in dp[len(s1)][len(s2)].
# Here's the Python implementation:


def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

# Example usage
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of LCS:", lcs(s1, s2))
