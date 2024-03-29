N = int(input())
dp = [0] * (1001)

for i in range(1, N+1):
    dp[i] = i % 2

if dp[N] == 1:
    print("SK")
else:
    print("CY")
