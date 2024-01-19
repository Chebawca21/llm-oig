import numpy as np

def calculate_distance(city1, city2):
    return np.abs(city1[0] - city2[0]) + np.abs(city1[1] - city2[1])

def main():
    # Step 1: Read input values
    n, m = map(int, input().split())
    
    cities = []
    for _ in range(n):
        cities.append(tuple(map(int, input().split())))
    
    byte_path = list(map(int, input().split()))

    # Step 2: Calculate the distance
    total_distance = 0
    for i in range(m - 1):
        city1 = cities[byte_path[i] - 1]
        city2 = cities[byte_path[i + 1] - 1]
        total_distance += calculate_distance(city1, city2)

    # Add the distance from the last city back to the starting city
    total_distance += calculate_distance(cities[byte_path[-1] - 1], cities[byte_path[0] - 1])

    # Step 3: Output the result
    print(total_distance)

if __name__ == "__main__":
    main()
