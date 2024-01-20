import numpy as np

def count_strings(n, heights):
    heights = np.array(heights)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if np.all(heights[i+1:j] < min(heights[i], heights[j])):
                count += 1

    return count

# Reading input
n = int(input())
heights = list(map(int, input().split()))

# Calculating and printing the result
result = count_strings(n, heights)
print(result)
