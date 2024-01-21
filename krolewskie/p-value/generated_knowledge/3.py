import numpy as np

def count_ones(binary_str):
    return np.sum(np.array(list(binary_str), dtype=int))

def find_kth_royal_number(k):
    count = 0
    number = 0
    while count < k:
        binary_representation = bin(number)[2:]
        ones_count = count_ones(binary_representation)
        if ones_count % 2 == 0:
            count += 1
        number += 1
    return number - 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
