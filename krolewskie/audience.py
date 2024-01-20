import numpy as np

def find_kth_royal_number(k):
    # Use numpy to find the next royal number efficiently
    binary_representation = np.binary_repr(k-1)
    
    # Count the number of ones in the binary representation
    count_ones = binary_representation.count('1')
    
    # If the count is odd, add 1 to make it even
    if count_ones % 2 != 0:
        k += 1
    
    return k

def main():
    t = int(input())
    
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
