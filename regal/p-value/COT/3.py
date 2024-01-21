import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Iterate over shelves and count the number of balls in each box
    for i, shelf in enumerate(shelves):
        boxes[i] = len(shelf)

    # Sort the boxes based on the number of balls
    sorted_indices = np.argsort(boxes)

    # Create a list to store the organized shelves
    organized_shelves = []

    # Populate the organized shelves list based on the sorted indices
    for index in sorted_indices:
        organized_shelves.append(shelves[index])

    return organized_shelves

if __name__ == "__main__":
    # Read input
    n = int(input())
    shelves = [input().strip() for _ in range(n)]

    # Organize the boxes and print the result
    result = organize_boxes(n, shelves)
    for shelf in result:
        print(shelf)
