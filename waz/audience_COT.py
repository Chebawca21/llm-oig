import numpy as np

def solve_snake_problem(a, b, board, n, m, moves):
    board_array = np.array(board)
    masked_segments = set()
    output = []

    def get_color(x, y):
        return board_array[x - 1, y - 1]

    for move in moves:
        head_x, head_y = divmod(masked_segments.pop() if masked_segments else 1, b)
        
        if move == 'N':
            head_x -= 1
        elif move == 'S':
            head_x += 1
        elif move == 'W':
            head_y -= 1
        elif move == 'E':
            head_y += 1

        head_color = get_color(head_x, head_y)
        segment_colors = [get_color(*divmod(segment, b)) for segment in range(head_x * b + head_y, head_x * b + head_y + m)]

        masked_segments.update(set(segment_colors))
        masked_count = len(masked_segments)
        output.append(masked_count)

    return output

# Get input from the user
a, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(a)]
n, m = map(int, input().split())
moves = input()

# Call the solve function
result = solve_snake_problem(a, b, board, n, m, moves)

# Print the result
print(" ".join(map(str, result)))
