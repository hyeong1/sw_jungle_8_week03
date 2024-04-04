string_a = ' ' + input()
string_b = ' ' + input()
dp = [[0] * 4001 for _ in range(4001)]

ans = 0
for i in range(1, len(string_b)):
    for j in range(1, len(string_a)):
        if string_a[j] == string_b[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        ans = max(ans, dp[i][j])

print(ans)
