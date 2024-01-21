import numpy as np

def sort_tomeks_collection(n, shelves):
    # Create an array to store the number of balls on each shelf
    ball_counts = np.zeros(n, dtype=int)

    # Calculate the number of balls on each shelf and store in the array
    for i, shelf in enumerate(shelves):
        ball_counts[i] = len(shelf)

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(ball_counts)

    # Create the sorted collection using the sorted indices
    sorted_collection = [shelves[i] for i in sorted_indices]

    return sorted_collection

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Sort and print the result
sorted_collection = sort_tomeks_collection(n, shelves)
for shelf in sorted_collection:
    print(shelf)
