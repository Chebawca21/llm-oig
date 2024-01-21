import numpy as np

def count_ones(binary_str):
    return binary_str.count('1')

def find_kth_royal_number(k):
    count = 0
    num = 0

    while True:
        binary_representation = np.binary_repr(num)
        if count_ones(binary_representation) % 2 == 0:
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
