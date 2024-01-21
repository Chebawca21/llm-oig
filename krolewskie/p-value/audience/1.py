import numpy as np

def find_kth_royal_number(k):
    # The k-th royal number can be obtained by setting the (k-1)-th bit to 1
    binary_representation = '1' + '0' * (k - 1)
    return int(binary_representation, 2)

def main():
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
