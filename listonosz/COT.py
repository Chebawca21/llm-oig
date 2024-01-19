import numpy as np

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_path_distance(n, m, cities, path):
    city_coordinates = np.array(cities)
    total_distance = 0

    for i in range(m - 1):
        start_city = path[i] - 1
        end_city = path[i + 1] - 1

        total_distance += distance(
            city_coordinates[start_city, 0],
            city_coordinates[start_city, 1],
            city_coordinates[end_city, 0],
            city_coordinates[end_city, 1]
        )

    # Add the distance from the last city back to the sorting center
    total_distance += distance(
        city_coordinates[path[-1] - 1, 0],
        city_coordinates[path[-1] - 1, 1],
        city_coordinates[path[0] - 1, 0],
        city_coordinates[path[0] - 1, 1]
    )

    return total_distance

# Example input
n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
path = list(map(int, input().split()))

# Calculate and print the distance
result = calculate_path_distance(n, m, cities, path)
print(result)