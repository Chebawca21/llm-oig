import numpy as np

def organize_boxes(n, shelves):
    # Create an array to store the count of balls in each box
    ball_counts = np.zeros(n, dtype=int)

    # Calculate the count of balls in each box
    for i, shelf in enumerate(shelves):
        ball_counts[i] = len(shelf)

    # Get the indices of sorted ball counts
    sorted_indices = np.argsort(ball_counts)

    # Organize the shelves based on the sorted indices
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)
