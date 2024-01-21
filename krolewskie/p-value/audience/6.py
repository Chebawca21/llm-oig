import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(k)[2:]  # Get binary representation without the '0b' prefix
    count_ones = np.count_nonzero([int(bit) for bit in binary_representation])
    return k + (count_ones % 2)

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
