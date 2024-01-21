import numpy as np

def sort_boxes(n, shelves):
    # Create an array to store the number of balls in each box
    ball_counts = np.zeros(n, dtype=int)

    # Count the number of balls in each box and store in ball_counts array
    for i, shelf in enumerate(shelves):
        ball_counts[i] = len(shelf)

    # Sort the indices based on the number of balls in each box
    sorted_indices = np.argsort(ball_counts)

    # Arrange the shelves according to the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Output
sorted_shelves = sort_boxes(n, shelves)
for shelf in sorted_shelves:
    print(shelf)
