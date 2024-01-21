import numpy as np

def count_ones(binary_str):
    return np.sum([int(bit) for bit in binary_str])

def find_kth_royal_number(k):
    count = 0
    num = 0
    while True:
        binary_representation = np.binary_repr(num)
        ones_count = count_ones(binary_representation)
        
        if ones_count % 2 == 0:
            count += 1

        if count == k:
            return num

        num += 1

# Read the number of queries
t = int(input())

# Process each query
for _ in range(t):
    k = int(input())
    result = find_kth_royal_number(k)
    print(result)