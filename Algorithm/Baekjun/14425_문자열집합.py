import sys

# KB / 160ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_14425.txt')

N, M = map(int, input().split())
M_dict = {}

res = 0
N_arr = set(input() for _ in range(N))
for _ in range(M):
    word = input()
    if word in M_dict.keys():
        M_dict[word] += 1
    else:
        M_dict[word] = 1
M_arr = set(M_dict.keys())

crossed = N_arr & M_arr
for word in crossed:
    res += M_dict[word]

print(res)
