import numpy as np

def max_hirsch_index(n, t, works, times):
    works.sort(key=lambda x: (x[1], -x[0]), reverse=True)  # Sort works by time and citations

    dp = np.zeros((n + 1, t + 1), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            dp[i, j] = dp[i - 1, j]
            if j >= works[i - 1][1]:
                dp[i, j] = max(dp[i, j], dp[i - 1, j - works[i - 1][1]] + min(i, works[i - 1][0]))

    result = []
    for z in times:
        result.append(dp[n, min(z, t)])

    return result

# Input processing
n, t = map(int, input().split())
works = [tuple(map(int, input().split())) for _ in range(n)]
times = [int(input()) for _ in range(t)]

# Calculate and print the output
output = max_hirsch_index(n, t, works, times)
for res in output:
    print(res)
