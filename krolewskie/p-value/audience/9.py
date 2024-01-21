import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(k)[2:]
    return int('1' + '0' * (len(binary_representation) - 1), 2)

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
