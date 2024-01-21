import numpy as np

def find_kth_royal_number(k):
    count = 0
    number = 0
    
    while True:
        binary_representation = np.binary_repr(number)
        ones_count = np.count_nonzero([int(digit) for digit in binary_representation])
        
        if ones_count % 2 == 0:
            count += 1
        
        if count == k:
            return number
        
        number += 1

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
