import numpy as np

def byte_land_distance(n, m, cities, order):
    # Create a numpy array for cities for efficient calculations
    cities_array = np.array(cities)

    total_distance = 0
    for i in range(m - 1):
        # Calculate distance using the given formula
        distance = np.abs(cities_array[order[i] - 1, 0] - cities_array[order[i + 1] - 1, 0]) + \
                   np.abs(cities_array[order[i] - 1, 1] - cities_array[order[i + 1] - 1, 1])
        total_distance += distance

    # Add distance to return to the starting city
    total_distance += np.abs(cities_array[order[-1] - 1, 0] - cities_array[order[0] - 1, 0]) + \
                     np.abs(cities_array[order[-1] - 1, 1] - cities_array[order[0] - 1, 1])

    return total_distance

# Read input
n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

# Calculate and print the result
result = byte_land_distance(n, m, cities, order)
print(result)
