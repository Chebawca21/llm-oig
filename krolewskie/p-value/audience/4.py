import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(k - 1)[2:]
    num_ones = np.count_nonzero([int(bit) for bit in binary_representation])
    if num_ones % 2 == 0:
        return k
    else:
        return int('1' + binary_representation, 2)

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
