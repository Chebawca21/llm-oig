import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(k // 2)[2:]
    royal_number = int('10' + binary_representation, 2)
    return royal_number

def main():
    t = int(input().strip())
    
    for _ in range(t):
        k = int(input().strip())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
