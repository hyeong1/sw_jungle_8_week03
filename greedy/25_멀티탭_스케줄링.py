import sys

N, K = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))

use = []
cnt = 0
for i in range(K):
    if seq[i] not in use:
        if len(use) < N:
            use.append(seq[i])
            continue

        again = []  # 나중에 다시 사용 하는지 체크
        for u in use:
            if u in seq[i:]:
                again.append(seq[i:].index(u))
            else:
                again.append(101)  # K는 최대 100
        out = again.index(max(again))
        use.remove(use[out])
        use.append(seq[i])
        cnt += 1

print(cnt)
