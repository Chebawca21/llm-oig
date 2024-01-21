import numpy as np

def sort_tomeks_collection(n, shelves):
    # Create a numpy array to store the number of balls in each box
    num_balls = np.zeros(n, dtype=int)

    # Calculate the number of balls in each box and store in the numpy array
    for i, shelf in enumerate(shelves):
        num_balls[i] = len(shelf)

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(num_balls)

    # Create the sorted collection using the sorted indices
    sorted_collection = [shelves[i] for i in sorted_indices]

    return sorted_collection

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Get the sorted collection
sorted_collection = sort_tomeks_collection(n, shelves)

# Print the sorted collection
for shelf in sorted_collection:
    print(shelf)
