import sys

# KB / ms
# input = sys.stdin.readline
'''
a값은 소수점 버린거 빼고 나머지값이 할당돼야 함
'''

sys.stdin = open('input_20057.txt')

def Tornado():
    global r, c, d, l

    while True:  # (0, 0)에 도착할 때까지
        for _ in range(2):  # 같은 길이로 두 번씩
            for _ in range(l):  # 길이 횟수만큼 실행
                r, c = r + dr[d], c + dc[d]
                if (r, c) == (0, -1):
                    return
                sand = arr[r][c]
                remain = arr[r][c]

                if sand:
                    # 방향 +1
                    nr, nc = r + dr[(d+1)%4], c + dc[(d+1)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.07)
                    remain -= int(sand * 0.07)
                    nr, nc = r + 2*dr[(d+1)%4], c + 2*dc[(d+1)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.02)
                    remain -= int(sand * 0.02)
                    nr, nc = r + dr[(d+1)%4] + dr[d], c + dc[(d+1)%4] + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.1)
                    remain -= int(sand * 0.1)
                    nr, nc = r + dr[(d+1)%4] + dr[(d+2)%4], c + dc[(d+1)%4] + dc[(d+2)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.01)
                    remain -= int(sand * 0.01)

                    # 방향 -1
                    nr, nc = r + dr[(d+3)%4], c + dc[(d+3)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.07)
                    remain -= int(sand * 0.07)
                    nr, nc = r + 2*dr[(d+3)%4], c + 2*dc[(d+3)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.02)
                    remain -= int(sand * 0.02)
                    nr, nc = r + dr[(d+3)%4] + dr[d], c + dc[(d+3)%4] + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.1)
                    remain -= int(sand * 0.1)
                    nr, nc = r + dr[(d+3)%4] + dr[(d+2)%4], c + dc[(d+3)%4] + dc[(d+2)%4]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.01)
                    remain -= int(sand * 0.01)

                    # 방향 그대로
                    nr, nc = r + 2*dr[d], c + 2*dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += int(sand * 0.05)
                    remain -= int(sand * 0.05)
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += remain
                    arr[r][c] = 0  # y의 모래는 0으로
            d = (d + 1) % 4
        l += 1

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]  # 좌하우상
    r, c, d, l = N//2, N//2, 0, 1  # 행, 열, 방향, 길이
    org_sand = sum(sum(arr, []))

    Tornado()
    print(org_sand - sum(sum(arr, [])))





