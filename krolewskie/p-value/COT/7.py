import numpy as np

def count_ones_in_binary(num):
    return bin(num).count('1')

def find_kth_royal_number(k):
    count = 0
    num = 0

    while True:
        if count_ones_in_binary(num) % 2 == 0:
            count += 1

        if count == k:
            return num

        num += 1

# Read the number of queries
t = int(input().strip())

# Process each query
for _ in range(t):
    k = int(input().strip())
    royal_number = find_kth_royal_number(k)
    print(royal_number)
