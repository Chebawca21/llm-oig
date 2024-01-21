import numpy as np

# Function to sort boxes and return the sorted collection
def sort_boxes(n, shelves):
    # Convert the shelves to a numpy array for easy sorting
    boxes = np.array([(len(shelf), shelf) for shelf in shelves], dtype=[('count', int), ('content', 'U10')])
    sorted_boxes = np.sort(boxes, order=['count', 'content'])

    # Extract the sorted contents
    sorted_contents = [box['content'] for box in sorted_boxes]

    return sorted_contents

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Solve the task and print the result
result = sort_boxes(n, shelves)
for content in result:
    print(content)
