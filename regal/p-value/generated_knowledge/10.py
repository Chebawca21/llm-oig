import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    balls_count = np.zeros(n, dtype=int)

    # Calculate the number of balls in each box
    for i, shelf in enumerate(shelves):
        balls_count[i] = len(shelf)

    # Sort the shelves based on the number of balls in each box
    sorted_indices = np.argsort(balls_count)

    # Organize the shelves according to the sorted indices
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Get the organized shelves
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)
