import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return binary_representation.count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    num = 0
    
    while len(royal_numbers) < k:
        if count_ones_in_binary(num) % 2 == 0:
            royal_numbers.append(num)
        num += 1
    
    return royal_numbers[-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
