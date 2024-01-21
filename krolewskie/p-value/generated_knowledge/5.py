import numpy as np

def count_ones(binary_representation):
    return np.count_nonzero(np.array(list(binary_representation)) == '1')

def find_kth_royal_number(k):
    count = 0
    number = 0
    
    while True:
        binary_representation = bin(number)[2:]
        ones_count = count_ones(binary_representation)
        
        if ones_count % 2 == 0:
            count += 1
        
        if count == k:
            return number
        
        number += 1

def main():
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
