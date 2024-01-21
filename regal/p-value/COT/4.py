import numpy as np

def organize_boxes(n, shelves):
    # Calculate the number of balls on each shelf
    ball_counts = np.array([sum(map(lambda x: 1 if x == 'O' else 0, shelf)) for shelf in shelves])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(ball_counts)

    # Organize the shelves according to the sorted indices
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
result = organize_boxes(n, shelves)

# Print the organized collection
for shelf in result:
    print(shelf)
