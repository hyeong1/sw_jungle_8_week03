import sys

W = int(input())
weight = list(map(int, sys.stdin.readline().split()))
B = int(input())
ball = list(map(int, sys.stdin.readline().split()))

max_weight = sum(weight)
dp = [0] * (max_weight + 1)
dp[0] = 1
dp[weight[0]] = 1

for i in range(1, W):  # 추 배열
    temp = []
    for j in range(max_weight, -1, -1):  # 현재까지 가능한 무게들
        if dp[j]:
            temp.append(j)
            temp.append(j + weight[i])
            temp.append(abs(j - weight[i]))
    for t in temp:
        dp[t] = 1

for b in ball:
    if b > max_weight:
        print('N', end=" ")
    elif dp[b]:
        print('Y', end=" ")
    else:
        print('N', end=" ")
