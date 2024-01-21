import numpy as np

def organize_boxes(n, shelves):
    # Calculate the sum of 'O' characters for each shelf
    sums = np.array([shelf.count('O') for shelf in shelves])

    # Sort the indices based on the sum of 'O' characters
    sorted_indices = np.argsort(sums)

    # Arrange the shelves according to the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Example usage
if __name__ == "__main__":
    # Read input
    n = int(input())
    shelves = [input().strip() for _ in range(n)]

    # Get the organized collection
    organized_collection = organize_boxes(n, shelves)

    # Print the result
    for shelf in organized_collection:
        print(shelf)
