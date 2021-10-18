import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
'''
1 : 사람
2~10 : 계단입구(길이)
'''

def cal_time(stair, p):

    if not p:
        return 0

    Q = []
    i = 
    for i in range(len(p)):


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())  # 방의 한 변 길이
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지도
    res = 987654321  # 모든 사람 이동완료 최소 시간
    s = []  # 계단 2개(행, 열, 길이)
    p = []  # 사람 위치(행, 열, 1번계단 시간, 2번계단 시간, 그 차이)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                p.append([i, j, 0, 0, 0])
            elif arr[i][j] > 1:
                s.append((i, j, arr[i][j]))

    for i in range(len(p)):
        p[i][2] = s[0][2] + abs(p[i][0] - s[0][0]) + abs(p[i][1] - s[0][1])
        p[i][3] = s[1][2] + abs(p[i][0] - s[1][0]) + abs(p[i][1] - s[1][1])
        p[i][4] = p[i][2] - p[i][3]

    p_choose = sorted(p, key=lambda x: x[4])
    # p_time1 = sorted(p_choose, key=lambda x: x[1][2])
    # p_time2 = sorted(p_choose, key=lambda x: x[1][3])
    print(p_choose)
    # print(p_time1)
    for i in range(1, len(p)+1):
        time = cal_time(1, sorted(p_choose[:i], key=lambda x: x[1][2])) + cal_time(2, sorted(p_choose[i:], key=lambda x: x[1][3]))
        if res < time:
            break

    print('#{} {}'.format(tc, res))