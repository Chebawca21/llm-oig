import numpy as np

def sort_tomeks_collection(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    num_balls = np.zeros(n, dtype=int)

    # Calculate the number of balls on each shelf and store in the numpy array
    for i in range(n):
        num_balls[i] = len(shelves[i])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(num_balls)

    # Display the sorted collection
    for i in sorted_indices:
        print(shelves[i])

# Example usage
if __name__ == "__main__":
    n = int(input())
    shelves = [input().strip() for _ in range(n)]

    sort_tomeks_collection(n, shelves)
