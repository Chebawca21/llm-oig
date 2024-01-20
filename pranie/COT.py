import numpy as np

def count_strings(n, heights):
    # Convert heights to numpy array
    heights = np.array(heights)

    # Initialize a counter for the number of strings
    string_count = 0

    # Iterate through all possible pairs of stakes
    for i in range(n):
        for j in range(i + 1, n):
            # Check if all stakes between i and j are lower than min(xi, xj)
            if np.all(heights[i+1:j] < min(heights[i], heights[j])):
                # Increment the string count if the condition is met
                string_count += 1

    return string_count

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
result = count_strings(n, heights)
print(result)
