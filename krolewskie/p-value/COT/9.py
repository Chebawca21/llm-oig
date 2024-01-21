import numpy as np

def count_ones_in_binary(num):
    # Count the number of ones in the binary representation of num
    return bin(num).count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    num = 0

    while len(royal_numbers) < k:
        if count_ones_in_binary(num) % 2 == 0:
            royal_numbers.append(num)
        num += 1

    return royal_numbers[-1]

if __name__ == "__main__":
    # Read the number of queries
    t = int(input())

    # Process each query
    for _ in range(t):
        # Read the k-th royal number query
        k = int(input())

        # Find and print the k-th royal number
        result = find_kth_royal_number(k)
        print(result)
