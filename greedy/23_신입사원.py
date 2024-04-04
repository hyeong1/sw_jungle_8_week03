import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    score.sort()  # 서류 성적 순으로 정렬

    max_score = score[0][1]  # 기준은 서류 성적 1등
    cnt = 1  # 서류 성적 1등은 무조건 포함
    for i in range(1, N):
        if max_score > score[i][1]:
            cnt += 1
            max_score = score[i][1]

    print(cnt)
