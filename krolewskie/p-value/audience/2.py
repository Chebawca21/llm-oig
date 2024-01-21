import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return np.sum([int(bit) for bit in binary_representation])

def find_kth_royal_number(k):
    count = 0
    num = 0
    while count < k:
        if count_ones_in_binary(num) % 2 == 0:
            count += 1
        num += 1
    return num

# Input reading
t = int(input())
queries = [int(input()) for _ in range(t)]

# Output
for query in queries:
    result = find_kth_royal_number(query)
    print(result)
