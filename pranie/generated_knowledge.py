import numpy as np

def count_strings(n, heights):
    # Create an array to store the number of strings between each pair of stakes
    num_strings = np.zeros((n, n), dtype=int)

    # Initialize the result counter
    result = 0

    # Iterate through stake pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if all stakes between i and j are lower than min(xi, xj)
            if np.all(heights[i+1:j] < min(heights[i], heights[j])):
                # Calculate the height of the string
                string_height = min(heights[i], heights[j])

                # Store the number of strings between i and j
                num_strings[i, j] = string_height

                # Increment the result counter
                result += 1

    return result

# Example usage
if __name__ == "__main__":
    # Read input
    n = int(input())
    heights = np.array(list(map(int, input().split())))

    # Calculate and print the result
    result = count_strings(n, heights)
    print(result)