import numpy as np

def count_ones_in_binary(n):
    return bin(n).count('1')

def find_kth_royal_number(k):
    royal_numbers = []
    num = 0
    
    while len(royal_numbers) < k:
        if count_ones_in_binary(num) % 2 == 0:
            royal_numbers.append(num)
        num += 1
    
    return royal_numbers

# Input reading
t = int(input())
queries = [int(input()) for _ in range(t)]

# Finding and printing the k-th royal numbers
for k in queries:
    royal_numbers = find_kth_royal_number(k)
    print(royal_numbers[-1])  # Print the last element as it corresponds to the k-th royal number
