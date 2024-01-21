import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    num_balls = np.zeros(n, dtype=int)

    # Fill the num_balls array based on the input shelves
    for i, shelf in enumerate(shelves):
        num_balls[i] = len(shelf)

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(num_balls)
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Call the function and print the output
result = organize_boxes(n, shelves)
for shelf in result:
    print(shelf)
