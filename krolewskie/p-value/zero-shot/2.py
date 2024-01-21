import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return binary_representation.count('1')

def find_kth_royal_number(k):
    num = 0
    while True:
        if count_ones_in_binary(num) % 2 == 0:
            k -= 1
        if k == 0:
            return num
        num += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        royal_number = find_kth_royal_number(k)
        print(royal_number)
