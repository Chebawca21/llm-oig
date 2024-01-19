import numpy as np

def count_ones(binary_representation):
    return np.sum([int(bit) for bit in binary_representation])

def find_kth_royal_number(k):
    current_number = 0
    while True:
        binary_representation = bin(current_number)[2:]
        ones_count = count_ones(binary_representation)
        if ones_count % 2 == 0:
            k -= 1
            if k == 0:
                return current_number
        current_number += 1

if __name__ == "__main__":
    # Read the number of queries
    t = int(input())

    # Process each query
    for _ in range(t):
        k = int(input())
        royal_number = find_kth_royal_number(k)
        print(royal_number)