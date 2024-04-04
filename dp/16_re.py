import sys

N, K = map(int, input().split())
goods = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(K+1)]

for j in range(1, N+1):
    for i in range(1, K+1):
        w, v = goods[j]
        if w > i:  # 넣을 수 없음
            dp[i][j] = dp[i][j-1]  # 현재 무게에서 지금 물건 안 넣은 최대 가치 유지
        else:  # 넣을 수 있음
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1] + v)  # 지금 물건 안넣은 가치에서 현재 가치 더하는 거니까 j도 -1 해줌

for d in dp:
    print(d)
print(dp[-1][-1])
