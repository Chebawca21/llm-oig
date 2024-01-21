import numpy as np

# Function to organize shelves
def organize_shelves(n, shelves):
    # Convert the shelves to a numpy array
    shelves_array = np.array(shelves)

    # Count the number of balls in each box
    balls_count = np.array([sum(box == 'O' for box in shelf) for shelf in shelves_array])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(balls_count)
    sorted_shelves = shelves_array[sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize shelves and print the result
result = organize_shelves(n, shelves)
for shelf in result:
    print(shelf)
