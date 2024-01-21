import numpy as np

def count_ones(n):
    return bin(n).count('1')

def find_kth_royal_number(k):
    count = 0
    number = 0
    
    while count < k:
        if count_ones(number) % 2 == 0:
            count += 1
        number += 1
    
    return number

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
