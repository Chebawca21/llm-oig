import numpy as np

def calculate_masked_segments(a, b, board, n, m, moves):
    board = np.array(board)
    snake_segments = np.arange(1, m + 1)
    
    def get_masked_segments(head_position):
        x, y = head_position
        segments_at_positions = board[x - 1:x + m - 1, y - 1:y]
        return np.intersect1d(segments_at_positions, snake_segments)

    masked_segments_counts = []

    head_position = np.array([1, 1])

    for move in moves:
        if move == 'N':
            head_position[0] -= 1
        elif move == 'S':
            head_position[0] += 1
        elif move == 'W':
            head_position[1] -= 1
        elif move == 'E':
            head_position[1] += 1

        masked_segments = get_masked_segments(head_position)
        masked_segments_counts.append(len(masked_segments))

    return masked_segments_counts

# User input
a, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(a)]
n, m = map(int, input().split())
moves = input()

result = calculate_masked_segments(a, b, board, n, m, moves)
print(*result)
