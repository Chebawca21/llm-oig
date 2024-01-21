import numpy as np

def organize_boxes(n, shelves):
    # Convert the input shelves to a numpy array for easy sorting
    shelves_np = np.array(shelves, dtype=object)

    # Sort the shelves based on the number of balls in each box
    sorted_indices = np.argsort([len(box) for box in shelves_np])

    # Reorder the shelves based on the sorted indices
    sorted_shelves = shelves_np[sorted_indices]

    return list(sorted_shelves)

if __name__ == "__main__":
    # Read input
    n = int(input())
    shelves = [input().strip() for _ in range(n)]

    # Organize the boxes and print the result
    result = organize_boxes(n, shelves)
    for box in result:
        print(box)
