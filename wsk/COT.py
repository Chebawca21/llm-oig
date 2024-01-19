import numpy as np

def max_hirsch_index(n, t, works, query_times):
    works.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    dp = np.zeros((n + 1, t + 1), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            dp[i, j] = dp[i - 1, j]
            if j >= works[i - 1][1]:
                dp[i, j] = max(dp[i, j], dp[i - 1, j - works[i - 1][1]] + min(i, works[i - 1][0]))

    result = []
    for time in query_times:
        result.append(dp[n, min(time, t)])

    return result

# Read input
n, t = map(int, input().split())
works = [tuple(map(int, input().split())) for _ in range(n)]
query_times = [int(input()) for _ in range(t)]

# Calculate and print the result
result = max_hirsch_index(n, t, works, query_times)
for r in result:
    print(r)
