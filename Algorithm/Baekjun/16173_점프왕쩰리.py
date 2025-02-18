import sys

input = sys.stdin.readline

def dfs(row, col, N, arr, visited):
  if visited[row][col]:
    return

  visited[row][col] = 1
  if arr[row][col] == -1:
    return 'HaruHaru'
  
  jump_amount = arr[row][col]
  if row + jump_amount < N:
    res = dfs(row + jump_amount, col, N, arr, visited)
    if res == 'HaruHaru':
      return 'HaruHaru'
  if col + jump_amount < N:
    res = dfs(row, col + jump_amount, N, arr, visited)
    if res == 'HaruHaru':
      return 'HaruHaru'
  
  return 'Hing'      

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

res = dfs(0, 0, N, arr, visited)

print(res)