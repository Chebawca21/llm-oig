import numpy as np

def count_ones_in_binary(num):
    return bin(num).count('1')

def find_kth_royal_number(k):
    royal_number = 0
    while k > 0:
        royal_number += 1
        if count_ones_in_binary(royal_number) % 2 == 0:
            k -= 1
    return royal_number

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
