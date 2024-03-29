import sys

N = int(input())

dp = [float("inf")] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, N+1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[N] >= 5000:
    print(-1)
else:
    print(dp[N])
