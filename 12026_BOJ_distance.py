import sys
sys.stdin = open('input.txt', 'r')





for _ in range(5):
    N = int(input())
    road = input()

    # road[0] = 'B'
    # k칸만큼 k*k만큼의 에너지
    # 스택으로 가면서 스택에 O J 가 있고, 방문하지 않았다면 B가 있을때까지 쭉 간다.
    # B를 만나면
    # 스택으로 푸는 백트래킹
    for i in range(1, N):
        for j in range(i):
            if (road[i] == 'B' and road[j] == 'J') or (road[i] == 'O' and road[j] == 'B') or (road[i] == 'J' and road[j] == 'O'):





'''
BJBBJOOOJJJJB
25 + 9 + 16
BJBOJOJOOJOBOOO
   9  9    25 9 
   
'''








'''
8
-1
50
1
52
'''