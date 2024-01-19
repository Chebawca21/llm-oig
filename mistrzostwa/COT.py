import numpy as np

def find_smallest_digit_to_divisible_by_three(number):
    digits = [int(d) if d.isdigit() else -1 for d in number]
    digit_sum = np.sum(digits)

    # Calculate the remainder when the sum of digits is divided by 3
    remainder = digit_sum % 3

    # Calculate the smallest digit needed to make the number divisible by 3
    smallest_digit = (3 - remainder) % 3

    # If the remainder is already 0, return the smallest digit that doesn't change the sum
    if remainder == 0:
        return smallest_digit

    # Find the position of the question mark
    question_mark_position = digits.index(-1)

    # Adjust the smallest digit to avoid changing the sum unnecessarily
    adjusted_smallest_digit = (smallest_digit + digits[question_mark_position]) % 3

    return adjusted_smallest_digit

# Read input from standard input
input_number = input().strip()

# Find the smallest digit to make the number divisible by three
result = find_smallest_digit_to_divisible_by_three(input_number)

# Print the result
print(result)
