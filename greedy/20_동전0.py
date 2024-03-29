import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
check = 0
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for i in range(N-1, -1, -1):
    if coins[i] > K:
        continue
    while K >= coins[i]:
        check += K // coins[i]
        K %= coins[i]

print(check)
