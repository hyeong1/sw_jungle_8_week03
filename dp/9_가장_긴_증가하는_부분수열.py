N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(N):  # 현재 숫자 인덱스
    for j in range(i):  # 이전 숫자 인덱스
        if nums[j] < nums[i] and dp[i] < dp[j] + 1:
            dp[i] += 1

print(max(dp))
