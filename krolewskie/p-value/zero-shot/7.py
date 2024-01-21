import numpy as np

def count_set_bits(num):
    return bin(num).count('1')

def find_kth_royal_number(k):
    royal_count, num = 0, 0
    
    while True:
        if count_set_bits(num) % 2 == 0:
            royal_count += 1
            if royal_count == k:
                return num
        num += 1

def main():
    t = int(input())
    
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
