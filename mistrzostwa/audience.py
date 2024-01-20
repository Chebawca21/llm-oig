def find_digit_to_insert(number):
    n = len(number)

    # Iterate over all possible digits (0 to 9)
    for digit in range(10):
        if digit == int(number[0]):
            continue  # Skip the digit in the first position

        # Replace the question mark with the current digit
        new_number = number.replace('?', str(digit))

        # Check if the new number is divisible by 3
        if int(new_number) % 3 == 0:
            return digit  # Return the digit if divisible

    return -1  # If no digit is found, return -1 (should not happen)

# Input
number = input().strip()

# Output
result = find_digit_to_insert(number)
print(result)
