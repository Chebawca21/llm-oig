import numpy as np

def max_hirsch_index(n, t, articles, queries):
    articles.sort(key=lambda x: x[0], reverse=True)  # Sort articles by citation in descending order
    
    hirsch_index = np.zeros(n + 1, dtype=int)

    for i in range(n):
        hirsch_index[i + 1] = min(hirsch_index[i], articles[i][0])

    result = []
    for query in queries:
        max_hirsch = np.searchsorted(hirsch_index, query, side='right') - 1
        result.append(max_hirsch)

    return result

# Read input
n, t = map(int, input().split())
articles = [tuple(map(int, input().split())) for _ in range(n)]
queries = [int(input()) for _ in range(t)]

# Calculate and print the results
results = max_hirsch_index(n, t, articles, queries)
for res in results:
    print(res)
