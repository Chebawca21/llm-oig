import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(k)[2:]
    royal_binary = ''.join(binary_representation[i] for i in range(0, len(binary_representation), 2))
    royal_number = int(royal_binary, 2)
    return royal_number

t = int(input())
for _ in range(t):
    ki = int(input())
    result = find_kth_royal_number(ki)
    print(result)
