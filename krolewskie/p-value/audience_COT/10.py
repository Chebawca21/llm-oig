import numpy as np

def find_kth_royal_number(k):
    binary_representation = np.binary_repr(k)
    if binary_representation.count('1') % 2 == 0:
        return k
    else:
        # Find the next royal number with an even number of ones
        return k + 2**(len(binary_representation) - binary_representation.rfind('1') - 1)

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
