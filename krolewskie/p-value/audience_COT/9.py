import numpy as np

def generate_royal_numbers(limit):
    royal_numbers = []
    for i in range(limit):
        binary_representation = bin(i)[2:]
        count_ones = np.count_nonzero(np.array(list(binary_representation), dtype=int))
        if count_ones % 2 == 0:
            royal_numbers.append(i)
    return royal_numbers

def main():
    # Read the number of queries
    t = int(input())

    # Process each query
    for _ in range(t):
        # Read the k-th royal number query
        k = int(input())

        # Generate royal numbers up to 2 * k to ensure we have enough
        royal_numbers = generate_royal_numbers(2 * k)

        # Print the k-th royal number
        print(royal_numbers[k - 1])

if __name__ == "__main__":
    main()
