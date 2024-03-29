T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1

    for val in coins:
        for i in range(1, M+1):
            if i - val >= 0:
                dp[i] += dp[i - val]  # 경우의 수를 구하는 거라서 계속 합

    print(dp[M])
