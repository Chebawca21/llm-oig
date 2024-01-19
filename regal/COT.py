import numpy as np

def organize_boxes(n, shelves):
    # Create an array to store the number of balls on each shelf
    balls_count = np.zeros(n, dtype=int)

    # Calculate the number of balls on each shelf
    for i in range(n):
        balls_count[i] = len(shelves[i])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(balls_count)

    # Create an array to store the organized shelves
    organized_shelves = np.empty_like(shelves, dtype=object)

    # Arrange the shelves according to the sorted indices
    for i in range(n):
        organized_shelves[i] = shelves[sorted_indices[i]]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)
