import sys
from collections import deque

input = sys.stdin.readline

# sys.stdin = open('input_2178.txt')

dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]

def bfs(x, y):
    Q = deque([(x, y)])

    while Q:
        r, c = Q.popleft()
        if (r, c) == (N-1, M-1):
            return visited[r][c]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

# T = int(input())
# for _ in range(T):
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

visited[0][0] = 1

res = bfs(0, 0)
print(res)