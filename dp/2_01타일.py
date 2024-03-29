import sys

N = int(input())
if N == 1:
    print(1)
    sys.exit()
elif N == 2:
    print(2)
    sys.exit()

two_before = 1
one_before = 2

answer = 0
for _ in range(3, N+1):
    answer = (two_before + one_before) % 15746
    two_before = one_before
    one_before = answer

print(answer)
