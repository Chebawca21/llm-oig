import numpy as np

def organize_boxes(n, shelves):
    # Convert the input shelves to a numpy array for easier sorting
    shelves_array = np.array(shelves)

    # Calculate the number of balls in each box
    balls_count = np.array([len(box) for box in shelves_array])

    # Sort shelves_array based on balls_count in ascending order
    sorted_indices = np.argsort(balls_count)
    sorted_shelves = shelves_array[sorted_indices]

    # Print the sorted shelves
    for shelf in sorted_shelves:
        print(shelf)

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Call the function with the input data
organize_boxes(n, shelves)
