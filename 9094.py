T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    cnt = 0
    for a in range(1, N):
        for b in range(a+1, N):
            if (a*a + b*b + M) % (a*b) == 0:
                cnt += 1

    print(cnt)
