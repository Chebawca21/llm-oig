import numpy as np

def find_smallest_digit(number):
    min_digit = float('inf')

    for digit in range(10):
        replaced_number = int(number.replace('?', str(digit)))
        if replaced_number % 3 == 0 and digit < min_digit:
            min_digit = digit

    return min_digit

# Read input
number = input().strip()

# Find and print the smallest digit
result = find_smallest_digit(number)
print(result)