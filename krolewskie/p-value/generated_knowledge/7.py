import numpy as np

def count_ones(binary_rep):
    return np.count_nonzero(np.array(list(binary_rep), dtype=int))

def find_kth_royal_number(k):
    royal_count = 0
    i = 0
    while True:
        binary_rep = bin(i)[2:]
        ones_count = count_ones(binary_rep)
        
        if ones_count % 2 == 0:
            royal_count += 1

        if royal_count == k:
            return i
        
        i += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
