basic = ' ' + input()
check = ' ' + input()

dp = [[0] * len(check) for _ in range(len(basic))]
for i in range(1, len(basic)):
    for j in range(1, len(check)):
        if basic[i] == check[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
