import numpy as np

def count_ones(binary_representation):
    return np.sum(np.array(list(binary_representation), dtype=int))

def find_kth_royal_number(k):
    count = 0
    number = 0
    while True:
        binary_representation = bin(number)[2:]
        if count_ones(binary_representation) % 2 == 0:
            count += 1
            if count == k:
                return number
        number += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
