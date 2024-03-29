import sys

N = int(input())
dp = [[0] * 3 for _ in range(N+1)]
score = [0]
for _ in range(N):
    score.append(int(input()))
if N == 1:
    print(score[1])
    sys.exit()

dp[1][1] = score[1]
dp[1][2] = 0  # 1번째 계단을 2번만에 오는 경우는 없음
dp[2][1] = score[2]
dp[2][2] = score[1] + score[2]  # 2번째 계단을 2번만에 오는 경우 (첫 번째 계단 밟고 두 번째 계단 밟기)

for i in range(2, N+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + score[i]
    dp[i][2] = dp[i-1][1] + score[i]

print(max(dp[N][1], dp[N][2]))
