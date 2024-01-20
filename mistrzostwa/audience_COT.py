import numpy as np

def find_smallest_digit(num_str):
    num_digits = list(map(int, num_str.replace('?', '0')))
    
    # Calculate the sum of known digits
    digit_sum = np.sum(num_digits)
    
    # Find the remainder when the sum is divided by 3
    remainder = digit_sum % 3
    
    # Calculate the smallest digit needed to make the number divisible by 3
    smallest_digit = (3 - remainder) % 3
    
    return smallest_digit

# Read input
num_str = input().strip()

# Find and print the smallest digit
result = find_smallest_digit(num_str)
print(result)
