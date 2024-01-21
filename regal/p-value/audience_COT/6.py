import numpy as np

# Function to sort the shelves based on the number of balls
def organize_shelves(n, shelves):
    # Create an array to store the number of balls in each box
    balls_count = np.array([len(shelf) for shelf in shelves])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(balls_count)

    # Organize the shelves according to the sorted order
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves and print the result
organized_shelves = organize_shelves(n, shelves)
for shelf in organized_shelves:
    print(shelf)
