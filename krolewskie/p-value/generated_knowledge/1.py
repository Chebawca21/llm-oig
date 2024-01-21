import numpy as np

def count_ones(binary_repr):
    return np.count_nonzero(np.array(list(binary_repr), dtype=int))

def is_royal_number(number):
    binary_repr = bin(number)[2:]
    ones_count = count_ones(binary_repr)
    return ones_count % 2 == 0

def find_kth_royal_number(k):
    royal_numbers_found = 0
    number = 0

    while royal_numbers_found < k:
        if is_royal_number(number):
            royal_numbers_found += 1
        number += 1

    return number - 1  # Adjust for the last increment that exceeded k

def main():
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
