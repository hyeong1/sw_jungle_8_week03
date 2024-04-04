N = int(input())
child = [int(input()) for _ in range(N)]
dp = [1] * N

for i in range(N):
    for j in range(i):
        if child[j] < child[i] and dp[i] < dp[j] + 1:
            dp[i] += 1

print(N - max(dp))
