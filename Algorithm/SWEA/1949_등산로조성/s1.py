import sys
sys.stdin = open('input.txt')

# 산깎기는 나중에 적용
def dfs(r, c, l, chance): # r: 행, c: 열
    global result

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not visited[nr][nc] and 0 <= m[nr][nc]:
            if m[nr][nc] < m[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, l + 1, chance)
                visited[nr][nc] = 0
            elif chance and m[nr][nc] - K < m[r][c]:
                temp = m[nr][nc]
                m[nr][nc] = m[r][c] - 1
                visited[nr][nc] = 1
                dfs(nr, nc, l + 1, chance - 1)
                visited[nr][nc] = 0
                m[nr][nc] = temp

    if l > result:
        result = l

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())  #  N: 지도 한변 길이, K: 최대 공사 가능 깊이
    m = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    dr = [0, 1, 0, -1] # 우하좌상
    dc = [1, 0, -1, 0]
    result = 1

    # 가장 높은 봉우리 높이 구하기
    max_h = 0
    for i in range(N):
        temp_h = max(m[i])
        if temp_h > max_h:
            max_h = temp_h

    # 시작점 구하기
    start = []
    for i in range(N + 2):
        for j in range(N + 2):
            if m[i][j] == max_h:
                start.append((i, j))

    for s in start:
        visited[s[0]][s[1]] = 1
        dfs(s[0], s[1], 1, 1)
        visited[s[0]][s[1]] = 0

    print('#{} {}'.format(t, result))