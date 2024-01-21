import numpy as np

def count_ones_in_binary(num):
    # Count the number of ones in the binary representation of num
    return bin(num).count('1')

def find_kth_royal_number(k):
    royal_numbers = [0]  # Initialize with the first royal number

    current_number = 1
    while len(royal_numbers) < k:
        # Check if the current number has an even number of ones in its binary representation
        if count_ones_in_binary(current_number) % 2 == 0:
            royal_numbers.append(current_number)
        current_number += 1

    return royal_numbers[k - 1]

def main():
    t = int(input())  # Number of queries
    for _ in range(t):
        ki = int(input())  # Query about the k-th royal number
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
