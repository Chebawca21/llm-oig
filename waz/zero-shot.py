import numpy as np

def calculate_masked_segments(a, b, board_colors, n, m, snake_moves):
    board = np.array(board_colors)
    snake_positions = np.zeros((a, b), dtype=int)
    masked_segments = np.zeros(n, dtype=int)

    current_color = 1
    snake_positions[0, 0] = current_color

    for move in snake_moves:
        if move == 'N':
            snake_positions = np.roll(snake_positions, shift=1, axis=0)
            snake_positions[0, :] = 0
            current_color += 1
            snake_positions[0, 0] = current_color
        elif move == 'S':
            snake_positions = np.roll(snake_positions, shift=-1, axis=0)
            snake_positions[-1, :] = 0
            current_color += 1
            snake_positions[-1, 0] = current_color
        elif move == 'W':
            snake_positions = np.roll(snake_positions, shift=1, axis=1)
            snake_positions[:, 0] = 0
            current_color += 1
            snake_positions[0, 0] = current_color
        elif move == 'E':
            snake_positions = np.roll(snake_positions, shift=-1, axis=1)
            snake_positions[:, -1] = 0
            current_color += 1
            snake_positions[0, -1] = current_color

        masked_segments[current_color - 2] = np.sum(np.logical_and(board == current_color, snake_positions > 0))

    return masked_segments

# User input
a, b = map(int, input().split())
board_colors = [list(map(int, input().split())) for _ in range(a)]
n, m = map(int, input().split())
snake_moves = input()

# Calculate and print the result
result = calculate_masked_segments(a, b, board_colors, n, m, snake_moves)
print(*result)
