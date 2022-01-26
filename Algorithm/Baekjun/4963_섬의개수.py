import sys
# sys.setrecursionlimit(10**9)
# KB / ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_.txt')


T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
