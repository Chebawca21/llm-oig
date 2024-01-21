import numpy as np

def organize_boxes(n, shelves):
    # Convert the list of shelves to a numpy array for easier manipulation
    shelves_array = np.array(shelves, dtype=object)

    # Calculate the number of balls on each shelf and sort the shelves accordingly
    sorted_indices = np.argsort([len(shelf) for shelf in shelves_array])
    shelves_array = shelves_array[sorted_indices]

    # Print the organized collection
    for shelf in shelves_array:
        print(''.join(shelf))

# Example usage:
if __name__ == "__main__":
    n = int(input())
    shelves = [input().strip() for _ in range(n)]

    organize_boxes(n, shelves)
