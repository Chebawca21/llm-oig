import numpy as np

def find_kth_royal_number(k):
    count = 0
    num = 0

    while True:
        binary_representation = np.binary_repr(num)
        count_ones = binary_representation.count('1')

        if count_ones % 2 == 0:
            count += 1

        if count == k:
            return num

        num += 1

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)
