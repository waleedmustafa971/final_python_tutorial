# Classic Greedy Algorithm Problems
# Fractional Knapsack Problem:

# Given a set of items, each with a weight and a value, determine the maximum value that can be obtained by selecting items such that the total weight doesn't exceed a given limit. Unlike the 0/1 knapsack problem, you can take fractions of items.
# Activity Selection Problem:

# Given a set of activities with start and end times, select the maximum number of activities that don't overlap.
# Huffman Coding:

# A greedy algorithm used for data compression. It generates an optimal prefix code that minimizes the overall length of encoded data.
# Let's implement a simple greedy algorithm to solve the Activity Selection Problem:

# Example: Activity Selection Problem
# In this problem, you're given a set of activities with start and finish times. Your goal is to select the maximum number of non-overlapping activities.

# Approach:
# Sort the activities by their finish time.
# Select the first activity from the sorted list.
# For each subsequent activity, if its start time is greater than or equal to the finish time of the previously selected activity, select it.
# Here's how you can implement it in Python:



# Function to perform Activity Selection
def activity_selection(activities):
    # Sort activities based on finish time
    activities.sort(key=lambda x: x[1])

    # The first activity is always selected
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    for i in range(1, len(activities)):
        # If the start time of the activity is greater than or equal to
        # the finish time of the last selected activity, select it
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities

# Example usage
activities = [(1, 3), (2, 5), (0, 6), (8, 9), (5, 7), (5, 9)]
selected = activity_selection(activities)
print("Selected activities:", selected)



# Explanation:
# The activities are sorted based on their finish times.
# We always select the first activity because it finishes the earliest.
# We then iterate through the remaining activities and select each one that starts after the last selected activity finishes.
# This is a classic example of a greedy algorithm where selecting the activity that finishes the earliest ensures that we leave enough time for the remaining activities, maximizing the total number of non-overlapping activities.