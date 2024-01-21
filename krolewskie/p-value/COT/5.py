import numpy as np

def count_ones(n):
    # Count the number of ones in the binary representation of n
    return bin(n).count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    num = 0

    while len(royal_numbers) < k:
        if count_ones(num) % 2 == 0:
            royal_numbers.append(num)
        num += 1

    return royal_numbers[k-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
