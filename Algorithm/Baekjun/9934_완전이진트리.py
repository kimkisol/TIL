import sys

# KB / ms Python3
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_9934.txt')


T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
