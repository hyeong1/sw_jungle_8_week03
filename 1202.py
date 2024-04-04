# 시간 초과
import sys


N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1], reverse=True)
bags = [int(sys.stdin.readline()) for _ in range(K)]

value = 0
for i in range(K):
    for j in range(len(arr)):
        if bags[i] >= arr[j][0]:
            value += arr[j][1]
            arr.remove(arr[j])
            break

print(value)
