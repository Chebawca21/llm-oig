import numpy as np

def count_ones_in_binary(num):
    binary_representation = bin(num)[2:]
    return np.count_nonzero(np.array(list(binary_representation), dtype=int))

def find_kth_royal_number(k):
    num = 0
    while k > 0:
        num += 1
        if count_ones_in_binary(num) % 2 == 0:
            k -= 1
    return num

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
