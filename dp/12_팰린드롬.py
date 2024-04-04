import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):  # 길이가 2인 팰린드롬 처리
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for cnt in range(N-2):  # 길이가 최소 3 이상 -> 팰린드롬 체크
    for i in range(N-2-cnt):
        j = i + 2 + cnt
        if nums[i] == nums[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
