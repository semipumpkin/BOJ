import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
sel = [0] * N
result = []
num = [1, 5, 10, 50]
def dfs(index, depth):

    if depth == N:
        total = sum(sel)
        if total not in result:
            result.append(total)
        # result.add(sum(sel))
        return

    for i in range(index, 4):
        if not sel[depth]:
            sel[depth] = num[i]
            dfs(i, depth + 1)
            sel[depth] = 0

dfs(0, 0)
print(len(result))


'''
4HN
4 + N - 1 C N

 I, V, X, L
 1, 5, 10, 50
II 2
IV 6
IX 11 
IL 51
VX 15
VL 
VV 10
XX
XL
LL


'''