N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [float("inf")] * (K + 1)
dp[0] = 0

for i in range(1, K+1):
    for val in coins:
        if i - val >= 0:
            dp[i] = min(dp[i], dp[i - val] + 1)

if dp[K] == float("inf"):
    print(-1)
else:
    print(dp[K])
