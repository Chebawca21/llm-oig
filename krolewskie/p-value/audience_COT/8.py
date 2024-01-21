import numpy as np

def generate_royal_numbers(limit):
    royal_numbers = []
    for i in range(limit):
        binary_representation = bin(i)[2:]
        count_ones = np.count_nonzero(np.array(list(binary_representation)) == '1')
        if count_ones % 2 == 0:
            royal_numbers.append(i)
    return royal_numbers

def main():
    t = int(input())
    queries = [int(input()) for _ in range(t)]

    limit = max(queries) * 2  # Setting a limit to generate royal numbers
    royal_numbers = generate_royal_numbers(limit)

    for query in queries:
        print(royal_numbers[query - 1])

if __name__ == "__main__":
    main()
