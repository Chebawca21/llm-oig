import numpy as np

def find_min_digit(number):
    digits = list(number)
    
    for i in range(10):
        digits_copy = digits.copy()
        digits_copy[1] = str(i)
        new_number = int(''.join(digits_copy))
        
        if new_number % 3 == 0:
            return i

# Read input
input_number = input().strip()

# Find and print the sought digit
result = find_min_digit(input_number)
print(result)