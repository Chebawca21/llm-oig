import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelves to a numpy array for efficient sorting
    shelves_array = np.array([len(shelf) for shelf in shelves])

    # Get the sorted indices of shelves_array
    sorted_indices = np.argsort(shelves_array)

    # Organize the shelves based on the sorted indices
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Input reading
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
organized_collection = organize_boxes(n, shelves)
for shelf in organized_collection:
    print(shelf)
