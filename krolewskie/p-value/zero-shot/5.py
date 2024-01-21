import numpy as np

def count_ones(binary_str):
    return sum(1 for bit in binary_str if bit == '1')

def find_kth_royal_number(k):
    count, num = 0, 0
    while True:
        ones_count = count_ones(bin(num)[2:])
        if ones_count % 2 == 0:
            count += 1
            if count == k:
                return num
        num += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
