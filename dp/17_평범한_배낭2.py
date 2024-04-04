import sys

N, M = map(int, input().split())
goods = [[0, 0]]
for _ in range(N):
    w, v, k = map(int, sys.stdin.readline().split())
    # K개의 [w, v]를 거듭 제곱 형태로 바꿈 -> logN 으로 단축
    cnt = 1
    while k > 0:
        temp = min(cnt, k)
        new_w = w * temp
        new_v = v * temp
        goods.append([new_w, new_v])
        cnt *= 2
        k -= temp

dp = [[0] * (len(goods)) for _ in range(M+1)]
for i in range(1, len(goods)):
    for j in range(1, M+1):
        w, v = goods[i]
        if w > j:
            dp[j][i] = dp[j][i-1]
        else:
            dp[j][i] = max(dp[j][i-1], dp[j-w][i-1] + v)

for d in dp:
    print(d)

print(dp[-1][-1])
