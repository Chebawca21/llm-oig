import numpy as np

def organize_boxes(n, shelves):
    # Create an array of tuples containing the index of the shelf and the number of balls
    boxes = [(i, len(shelf)) for i, shelf in enumerate(shelves)]
    
    # Sort the boxes based on the number of balls
    sorted_boxes = sorted(boxes, key=lambda x: x[1])
    
    # Create an empty array to represent the organized shelves
    organized_shelves = np.empty(n, dtype=object)
    
    # Populate the organized shelves based on the sorted boxes
    for i, (shelf_index, _) in enumerate(sorted_boxes):
        organized_shelves[i] = shelves[shelf_index]
    
    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)
