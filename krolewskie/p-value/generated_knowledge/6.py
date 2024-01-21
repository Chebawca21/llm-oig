import numpy as np

def count_ones_in_binary(num):
    # Convert the number to binary and count the number of ones
    binary_representation = bin(num)[2:]
    return np.count_nonzero(np.array(list(binary_representation), dtype=int))

def find_kth_royal_number(k):
    # Start checking from the first positive integer
    current_number = 0
    while True:
        # Check if the number is royal
        if count_ones_in_binary(current_number) % 2 == 0:
            k -= 1
            if k == 0:
                return current_number
        current_number += 1

# Read the number of queries
t = int(input())

# Process each query
for _ in range(t):
    k = int(input())
    result = find_kth_royal_number(k)
    print(result)
