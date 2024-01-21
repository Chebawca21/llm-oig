import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return np.count_nonzero(np.array(list(binary_representation), dtype=int))

def find_kth_royal_number(k):
    royal_number = 0
    while True:
        if count_ones_in_binary(royal_number) % 2 == 0:
            k -= 1
        if k == 0:
            return royal_number
        royal_number += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
