import numpy as np

def max_hirsch_index(n, t, articles, queries):
    articles.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    max_citations = np.zeros(n, dtype=int)
    prefix_sum = np.zeros(n, dtype=int)

    for i in range(n):
        max_citations[i] = articles[i][0]
        prefix_sum[i] = articles[i][1] if i == 0 else prefix_sum[i - 1] + articles[i][1]

    result = []

    for query_time in queries:
        left, right = 1, n
        max_hirsch = 0

        while left <= right:
            mid = (left + right) // 2

            total_time = prefix_sum[mid - 1]
            if total_time <= query_time:
                max_hirsch = mid
                left = mid + 1
            else:
                right = mid - 1

        result.append(max_citations[max_hirsch - 1] if max_hirsch > 0 else 0)

    return result

# Read input
n, t = map(int, input().split())
articles = [tuple(map(int, input().split())) for _ in range(n)]
queries = [int(input()) for _ in range(t)]

# Calculate and print the result
result = max_hirsch_index(n, t, articles, queries)
for res in result:
    print(res)
