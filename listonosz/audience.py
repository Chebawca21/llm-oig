import numpy as np

def calculate_distance(city1, city2):
    return np.abs(city1[0] - city2[0]) + np.abs(city1[1] - city2[1])

def main():
    n, m = map(int, input().split())
    
    cities = [tuple(map(int, input().split())) for _ in range(n)]
    
    order = list(map(int, input().split()))
    
    total_distance = 0
    
    for i in range(m - 1):
        total_distance += calculate_distance(cities[order[i] - 1], cities[order[i + 1] - 1])
    
    # Add the distance from the last city back to the sorting center
    total_distance += calculate_distance(cities[order[m - 1] - 1], cities[order[0] - 1])
    
    print(total_distance)

if __name__ == "__main__":
    main()
