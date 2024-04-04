import sys

string = input()
N = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

dp = [False] * (len(string) + 1)
dp[0] = True
for i in range(len(string)):
    for word in words:
        check = string[i:i + len(word)]
        if check != word:
            continue
        if dp[i]:
            dp[i + len(word)] = True  # 같으면

if dp[-1]:
    print(1)
else:
    print(0)
