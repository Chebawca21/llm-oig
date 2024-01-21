import numpy as np

# Step 1: Read input values
n = int(input().strip())
shelves = [input().strip() for _ in range(n)]

# Step 2: Create a list of tuples with descriptions and number of balls
boxes = [(shelf, shelf.count('O')) for shelf in shelves]

# Step 3: Sort the list of tuples based on the number of balls
sorted_boxes = np.array(sorted(boxes, key=lambda x: x[1]))

# Step 4: Print the sorted descriptions
for box in sorted_boxes[:, 0]:
    print(box)
