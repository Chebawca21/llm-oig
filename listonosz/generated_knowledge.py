import numpy as np

def calculate_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

def calculate_total_distance(cities, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += calculate_distance(cities[order[i] - 1], cities[order[i + 1] - 1])
    total_distance += calculate_distance(cities[order[-1] - 1], cities[order[0] - 1])
    return total_distance

def main():
    n, m = map(int, input().split())
    
    cities = []
    for _ in range(n):
        x, y = map(int, input().split())
        cities.append((x, y))
    
    order = list(map(int, input().split()))
    
    total_distance = calculate_total_distance(cities, order)
    
    print(total_distance)

if __name__ == "__main__":
    main()