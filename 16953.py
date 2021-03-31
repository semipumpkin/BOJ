import sys
sys.stdin = open("input.txt", "r")

for _ in range(3):
A, B = map(int, input().split())
count = 1
while len(str(B)) != len(str(A)):
    if str(B)[-1] == '1':
        B = B // 10
        count += 1
    else:
        B = B//2
        count += 1

# print(A, B, count)
while True:
    if B > A and B % 2 == 0:
        B = B // 2
        count += 1
    elif B == A:

        break
    else:
        count = -1
        break



print(count)