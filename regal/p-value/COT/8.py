import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelves to a numpy array for easy sorting
    shelves_array = np.array(shelves)

    # Calculate the number of balls on each shelf and sort the shelves accordingly
    sorted_indices = np.argsort([np.sum(np.array(list(shelf)) == 'O') for shelf in shelves_array])

    # Output the sorted shelves
    for index in sorted_indices:
        print(shelves_array[index])

# Example usage
if __name__ == "__main__":
    n = int(input())
    shelves = [input().strip() for _ in range(n)]
    organize_boxes(n, shelves)
