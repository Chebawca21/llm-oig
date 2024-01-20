import numpy as np

def count_strings(n, heights):
    heights = np.array(heights)
    left_min = np.maximum.accumulate(heights, axis=0)
    right_min = np.maximum.accumulate(heights[::-1], axis=0)[::-1]

    min_heights = np.minimum(left_min, right_min)

    return np.sum(heights > min_heights)

# Input
n = int(input())
heights = list(map(int, input().split()))

# Output
result = count_strings(n, heights)
print(result)
