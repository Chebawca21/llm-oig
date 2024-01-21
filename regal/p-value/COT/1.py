import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelves to a numpy array for easy sorting
    shelves_np = np.array(shelves)

    # Calculate the number of balls in each box and sort the indices accordingly
    sorted_indices = np.argsort([np.sum(np.array(list(box)) == 'O') for box in shelves_np])

    # Organize the shelves based on the sorted indices
    organized_shelves = shelves_np[sorted_indices]

    return organized_shelves

# Input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Output
result = organize_boxes(n, shelves)
for box in result:
    print(box)
