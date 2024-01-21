import numpy as np

def calculate_hirsch_index(n, t, works, queries):
    works.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    citations = np.zeros(n)
    
    for i in range(n):
        citations[i] = works[i][0]
    
    max_hirsch_indices = []
    
    for query_time in queries:
        total_time = 0
        hirsch_index = 0
        
        for i in range(n):
            if total_time + works[i][1] <= query_time:
                total_time += works[i][1]
                hirsch_index += 1
            else:
                break
        
        while hirsch_index < n and citations[hirsch_index] >= hirsch_index + 1:
            hirsch_index += 1
        
        max_hirsch_indices.append(hirsch_index)
    
    return max_hirsch_indices

# Sample input parsing
n, t = map(int, input().split())
works = [tuple(map(int, input().split())) for _ in range(n)]
queries = [int(input()) for _ in range(t)]

# Calculate and print the results
result = calculate_hirsch_index(n, t, works, queries)
for hirsch_index in result:
    print(hirsch_index)