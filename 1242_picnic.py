import sys
sys.stdin = open('input.txt', 'r')

K, N, M = map(int, input().split())

target = 0
while target != M:
    cnt = 0
    cnt += N // K
    N -= cnt

'''

1 2 3 4 5
  2
      2 
2   
        2   
    2 
'''