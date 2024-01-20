import numpy as np

def solve_snake_problem(a, b, board_colors, n, m, snake_moves):
    board = np.array(board_colors)
    snake_mask = np.zeros_like(board, dtype=int)
    snake_segments_masked = []

    head_position = (0, 0)

    for move in snake_moves:
        if move == 'N':
            head_position = (max(0, head_position[0] - 1), head_position[1])
        elif move == 'S':
            head_position = (min(a - 1, head_position[0] + 1), head_position[1])
        elif move == 'W':
            head_position = (head_position[0], max(0, head_position[1] - 1))
        elif move == 'E':
            head_position = (head_position[0], min(b - 1, head_position[1] + 1))

        snake_mask = np.where(board == head_position[1] + 1, 1, snake_mask)
        segments_masked = np.sum(snake_mask)
        snake_segments_masked.append(segments_masked)

    return snake_segments_masked

# Input
a, b = map(int, input().split())
board_colors = [list(map(int, input().split())) for _ in range(a)]
n, m = map(int, input().split())
snake_moves = input()

# Solve
result = solve_snake_problem(a, b, board_colors, n, m, snake_moves)

# Output
print(" ".join(map(str, result)))
