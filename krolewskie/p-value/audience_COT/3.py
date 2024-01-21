import numpy as np

def count_ones_in_binary(num):
    return bin(num).count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    current_number = 0

    while len(royal_numbers) < k:
        if count_ones_in_binary(current_number) % 2 == 0:
            royal_numbers.append(current_number)
        current_number += 1

    return royal_numbers[k - 1]

# Read the number of queries
t = int(input())

# Process each query
for _ in range(t):
    ki = int(input())
    result = find_kth_royal_number(ki)
    print(result)
