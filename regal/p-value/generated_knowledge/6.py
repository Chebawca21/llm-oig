import numpy as np

def sort_boxes(n, boxes):
    # Create a numpy array to store the number of balls in each box
    ball_counts = np.zeros(n, dtype=int)

    # Iterate through the input boxes and count the number of balls in each box
    for i in range(n):
        ball_counts[i] = len(boxes[i])

    # Get the indices that would sort the ball_counts array
    sorted_indices = np.argsort(ball_counts)

    # Create the sorted collection based on the sorted indices
    sorted_collection = [boxes[i] for i in sorted_indices]

    return sorted_collection

# Read input
n = int(input())
boxes = [input().strip() for _ in range(n)]

# Sort the boxes
sorted_collection = sort_boxes(n, boxes)

# Print the sorted collection
for box in sorted_collection:
    print(box)
