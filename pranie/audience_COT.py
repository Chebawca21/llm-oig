import numpy as np

def count_strings(n, heights):
    # Create a 2D array to store the minimum height between each pair of stakes
    min_heights = np.zeros((n, n), dtype=int)

    # Initialize the count of strings
    count = 0

    # Fill the min_heights array and count the strings
    for i in range(n):
        for j in range(i + 1, n):
            min_heights[i, j] = min(heights[i], heights[j])
            # Check if all stakes between i and j are lower than min(xi, xj)
            if all(heights[k] < min(heights[i], heights[j]) for k in range(i + 1, j)):
                count += 1

    return count

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
result = count_strings(n, heights)
print(result)
