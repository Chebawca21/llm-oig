import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelves to a numpy array for sorting based on the number of balls
    shelves_np = np.array(shelves)

    # Calculate the number of balls in each box
    num_balls_per_box = np.array([len(box) for box in shelves_np])

    # Sort shelves based on the number of balls
    sorted_indices = np.argsort(num_balls_per_box)

    # Organize the shelves according to the sorted order
    organized_shelves = shelves_np[sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Solve the task
result = organize_boxes(n, shelves)

# Print the result
for box in result:
    print(box)
