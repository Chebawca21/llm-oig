import numpy as np

def count_ones(binary_str):
    return np.sum([int(bit) for bit in binary_str])

def find_kth_royal_number(k):
    count = 0
    number = 0

    while True:
        binary_str = bin(number)[2:]
        ones_count = count_ones(binary_str)

        if ones_count % 2 == 0:
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
