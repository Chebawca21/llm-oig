import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return binary_representation.count('1')

def find_kth_royal_number(k):
    royal_number = 0
    while True:
        if count_ones_in_binary(royal_number) % 2 == 0:
            k -= 1
        if k == 0:
            return royal_number
        royal_number += 1

if __name__ == "__main__":
    # Read the number of queries
    t = int(input())

    # Process each query
    for _ in range(t):
        # Read the k-th royal number query
        kth_query = int(input())

        # Find and print the k-th royal number
        result = find_kth_royal_number(kth_query)
        print(result)
