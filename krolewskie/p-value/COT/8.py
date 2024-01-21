import numpy as np

def count_ones_in_binary(number):
    return bin(number).count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    number = 0
    while len(royal_numbers) < k:
        if count_ones_in_binary(number) % 2 == 0:
            royal_numbers.append(number)
        number += 1
    return royal_numbers[k - 1]

def main():
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
