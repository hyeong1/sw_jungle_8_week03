import sys
import heapq

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort()

cup_list = []
for i in range(N):
    limit, cup = arr[i]
    heapq.heappush(cup_list, cup)
    if limit < len(cup_list):
        heapq.heappop(cup_list)
        heapq.heappush(cup_list, cup)

print(sum(cup_list))
