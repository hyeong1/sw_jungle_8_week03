import sys

N = int(input())
reservation = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    reservation.append([start, end])
reservation.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev_end = 0
for start, end in reservation:
    if prev_end <= start:  # 이전 회의 끝나는 시간 보다 지금 회의 시작 시간이 같거나 이후 여야 가능
        cnt += 1
        prev_end = end

print(cnt)
