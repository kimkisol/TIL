import sys
from collections import deque
# sys.setrecursionlimit(10**9)
# KB / ms
# input = sys.stdin.readline
'''
가로, 세로 또는 대각선으로 연결되어 있는 사각형 => 섬으로 이어진 사각형!!
bfs는 Queue에 넣을때 visited 처리해줘야함
'''

sys.stdin = open('input_4963.txt')

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y):

    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        r, c = Q.popleft()

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and arr[nr][nc]:
                    visited[nr][nc] = 1  # 여기 visited 해줘야 헛수고 안함...
                    Q.append((nr, nc))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for r in range(h):
        for c in range(w):
            if arr[r][c] and not visited[r][c]:
                cnt += 1
                bfs(r, c)

    print(cnt)

