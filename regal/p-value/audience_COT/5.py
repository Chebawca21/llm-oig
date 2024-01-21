import numpy as np

# Read the input values
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Convert descriptions into a list of tuples (number of balls, description)
shelves_with_counts = [(len(shelf), shelf) for shelf in shelves]

# Sort the list of tuples based on the number of balls
sorted_shelves = np.array(sorted(shelves_with_counts, key=lambda x: x[0]))

# Output the sorted descriptions
for shelf in sorted_shelves[:, 1]:
    print(shelf)
