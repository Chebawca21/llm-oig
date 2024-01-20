import numpy as np

def organize_boxes(n, boxes):
    # Create a numpy array to store the number of balls in each box
    ball_counts = np.array([len(box) for box in boxes])

    # Sort the indices based on the number of balls
    sorted_indices = np.argsort(ball_counts)

    # Reorder the boxes based on the sorted indices
    sorted_boxes = [boxes[i] for i in sorted_indices]

    return sorted_boxes

# Read input
n = int(input())
boxes = [input().strip() for _ in range(n)]

# Solve the task
result = organize_boxes(n, boxes)

# Print the result
for box in result:
    print(box)
