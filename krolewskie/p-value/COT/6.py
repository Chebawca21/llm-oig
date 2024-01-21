import numpy as np

def count_ones(binary_repr):
    return sum(int(bit) for bit in binary_repr)

def find_kth_royal_number(k):
    royal_numbers = []
    num = 0

    while len(royal_numbers) < k:
        binary_repr = bin(num)[2:]
        if count_ones(binary_repr) % 2 == 0:
            royal_numbers.append(num)
        num += 1

    return royal_numbers[k - 1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
