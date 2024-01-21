import numpy as np

def calculate_masked_segments(board, snake_moves):
    a, b = board.shape
    n = len(snake_moves)
    masked_segments = np.zeros(n + 1, dtype=int)
    
    # Create a mask for each color on the board
    color_masks = [board == i for i in range(1, np.max(board) + 1)]
    
    # Initialize the snake's head position
    head_position = np.array([0, 0])
    
    for move_index, move in enumerate(snake_moves):
        if move == 'N':
            head_position[0] -= 1
        elif move == 'S':
            head_position[0] += 1
        elif move == 'W':
            head_position[1] -= 1
        elif move == 'E':
            head_position[1] += 1
        
        # Check if the snake's head is on a masked segment
        for color_mask in color_masks:
            if color_mask[tuple(head_position)]:
                masked_segments[move_index + 1] += 1
                break
    
    return masked_segments[1:]

# Read input
a, b = map(int, input().split())
board_colors = np.array([list(map(int, input().split())) for _ in range(a)])
n, m = map(int, input().split())
snake_moves = input()

# Calculate and print the result
result = calculate_masked_segments(board_colors, snake_moves)
print(' '.join(map(str, result)))