import sys
sys.stdin = open('input.txt', 'r')



def chicken_distance():
    global answer
    total = 0
    for house in houses:
        min_distance = 9999999
        for sel in sels:

            distance = abs(sel[0] - house[0]) + abs(sel[1] - house[1])
            if distance < min_distance:
                min_distance = distance
        total += min_distance
        if total > answer:
            return answer
    return total

def power_set(idx, n, k):
    global answer
    if len(sels) > k:

        return
    if idx == n:
        # return
        if len(sels) == k:
            # print(*sel)
            total = chicken_distance()
            if total < answer:
                answer = total
            return
        return
    power_set(idx+1, n, k)
    sels.append(chickens[idx])
    power_set(idx+1, n, k)
    sels.pop()



for _ in range(4):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    # print(city)
    chickens = []
    houses = []
    answer = 9999999

    for i in range(n):
        for j in range(n):
            if city[i][j] == 2:
                chickens.append([i, j])
            elif city[i][j]:
                houses.append([i, j])
    k = len(chickens)
    sels = []
    power_set(0, k, m)
    # print(sel)
    # print(houses)
    # print(chickens)
    print(answer)
