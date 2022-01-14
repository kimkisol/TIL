import sys
# sys.setrecursionlimit(10**9)
# KB / ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_14600.txt')


dr = []
dc = []

def dfs(r, c):
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and arr[nr][nc] > h:
                visited[nr][nc] = 1
                dfs(nr, nc)

T = int(input())

for _ in range(T):
    K = int(input())
    x, y = map(int, input().split())
    arr = [[0] * 2 ** K for _ in range(2 ** K)]
    arr[2 ** K - x][y - 1] = -1
    cnt = 2 ** K - 1

    print(arr)
    dfs(0, 0)
