import sys

N, K = map(int, input().split())
goods = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(goods)

dp = [[0] * (N + 1) for _ in range(K + 1)]
for j in range(1, N + 1):
    for i in range(1, K + 1):
        if goods[j-1][0] <= i:  # 넣을 수 있음
            dp[i][j] = max(dp[i][j-1], dp[i - goods[j-1][0]][j-1] + goods[j-1][1])
        else:
            dp[i][j] = dp[i][j-1]  # 못 넣으면 이전 최대 가치 유지

print(dp[-1][-1])
