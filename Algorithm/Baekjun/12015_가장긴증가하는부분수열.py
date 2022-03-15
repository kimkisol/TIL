import sys

# KB / ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_12015.txt')


def dfs(now, l, lst):
    global max_len

    print(lst)

    flag = False
    for j in range(now + 1, N):
        if arr[j] > arr[now]:
            flag = True
            dfs(j, l + 1, lst + [arr[j]])
    if not flag and l > max_len:
        max_len = l
        return


N = int(input())
arr = list(map(int, input().split()))
max_len = 1

for i in range(N - 1):
    if i <= N - max_len:
        print('i', i)
        dfs(i, 1, [arr[i]])

print(max_len)