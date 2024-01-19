import numpy as np

def organize_boxes(n, shelves):
    shelves_array = np.array([list(boxes) for boxes in shelves])
    balls_count = np.sum(shelves_array == 'O', axis=1)
    sorted_indices = np.argsort(balls_count)
    sorted_shelves = shelves_array[sorted_indices]
    result = [''.join(boxes) for boxes in sorted_shelves]
    return result

if __name__ == "__main__":
    n = int(input())
    shelves_input = [input().strip() for _ in range(n)]  # Ensure leading/trailing whitespaces are removed
    result = organize_boxes(n, shelves_input)
    for box in result:
        print(box)
