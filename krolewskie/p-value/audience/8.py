import numpy as np

def find_kth_royal_number(k):
    # Use numpy's binary representation and count the number of ones
    binary_representation = np.binary_repr(k)
    ones_count = binary_representation.count('1')
    
    # If the number of ones is odd, increment k until it becomes even
    while ones_count % 2 != 0:
        k += 1
        binary_representation = np.binary_repr(k)
        ones_count = binary_representation.count('1')
    
    return k

# Read the number of queries
t = int(input().strip())

# Process each query
for _ in range(t):
    ki = int(input().strip())
    result = find_kth_royal_number(ki)
    print(result)
