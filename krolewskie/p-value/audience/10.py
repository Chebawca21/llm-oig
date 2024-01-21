import numpy as np

def find_kth_royal_number(k):
    n = int(np.floor(np.log2(k)))
    royal_number = 0

    for i in range(n, -1, -1):
        if k >= 2**i:
            k -= 2**i
            royal_number += 2**i

    return royal_number

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ki = int(input())
        result = find_kth_royal_number(ki)
        print(result)
