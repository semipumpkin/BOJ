import sys
sys.stdin = open("input.txt", "r")


for _ in range(5):
    N = int(input())
    nums = list(map(int, input().split()))
    # nums를 돌며 값 + 1이 N보다 크면 안되는 거임
    #


'''
0 1 2 3 4
r = 0 5 
c = 5 0 

1 0 2 0 1
r1 r3 r2 c1 c2
c1 c3 c2 r1 r2

r = 3 2   
c = 2 3

'''
'''
2
0
0
8
0
'''