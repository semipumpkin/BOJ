import sys
sys.stdin = open("input.txt", "r")
s = input()
t = input()

a = len(t) * s
b = len(s) * t
# print(a)
# print(b)
if a == b:
    print(1)
else:
    print(0)
