import numpy as np

def count_ones(binary_str):
    return binary_str.count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    current_number = 0

    while len(royal_numbers) < k:
        binary_representation = bin(current_number)[2:]
        if count_ones(binary_representation) % 2 == 0:
            royal_numbers.append(current_number)
        current_number += 1

    return royal_numbers[-1]

if __name__ == "__main__":
    t = int(input())
    results = []

    for _ in range(t):
        ki = int(input())
        royal_number = find_kth_royal_number(ki)
        results.append(royal_number)

    for result in results:
        print(result)
