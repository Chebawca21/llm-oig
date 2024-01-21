import numpy as np

def organize_collection(n, shelves):
    boxes = np.zeros(n, dtype=int)
    for i, shelf in enumerate(shelves):
        boxes[i] = len(shelf)
    sorted_boxes = np.argsort(boxes)
    sorted_shelves = [shelves[i] for i in sorted_boxes]
    return sorted_shelves

if __name__ == "__main__":
    n = int(input())
    shelves = [input() for _ in range(n)]

    result = organize_collection(n, shelves)
    for shelf in result:
        print(shelf)
