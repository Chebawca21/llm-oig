import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelf descriptions to an array of ball counts
    ball_counts = np.array([len(shelf) for shelf in shelves])
    
    # Get the indices that would sort the ball_counts array
    sorted_indices = np.argsort(ball_counts)
    
    # Create a list to store the organized shelves
    organized_shelves = [shelves[i] for i in sorted_indices]
    
    return organized_shelves

# Input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
result = organize_boxes(n, shelves)

# Output
for shelf in result:
    print(shelf)
