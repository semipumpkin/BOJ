import sys
sys.stdin = open("input.txt", "r")

def reversing(string):
    temp = ''
    for i in range(len(string) - 1, -1, -1):
        temp += string[i]
        # print(string[i])
    return temp

# print(reversing('awef'))

S = input()
T = input()
# flag = 1
while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = reversing(T[:-1])
    # print(T)
if S == T:
    print(1)
else:
    print(0)


'''
B
BA
ABB
ABBA

BB
BBA
ABBA

'''