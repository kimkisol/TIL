import sys
sys.stdin = open('input.txt')


def dfs(node, connect, w_level, i, lst):
    if i != 0:
        if w_level == 1:
            print('        ' * w_level, end='')
        elif w_level > 1:
            for i in range(w_level):
                if i == 0:
                    print('        ', end='')
                    continue
                print(f'{lst[i]}           ', end='')

    zeros = '0' * (3 - len(str(node)))
    if tree[node]:
        if node == root:
            print(f'[{zeros}{node}] --', end='') # 자식이 있는 노드 출력
        else:
            print(f'{connect}-- [{zeros}{node}] --', end='')
        for i in range(len(tree[node])):
            connect = '+'
            x = '|'
            if len(tree[node]) == 1:
                connect = '-'
                x = ' '
            elif i == len(tree[node]) - 1:
                connect = 'L'
                x = ' '

            dfs(tree[node][i], connect, w_level + 1, i, lst + [x])
    else:
        print(f'{connect}-- [{zeros}{node}]') # 리프 노드 출력


l = list(map(int, input().split()))
N, E = len(l) // 2 + 1, len(l) // 2 # N: 노드의 수, E: 간선의 수

tree = {key:[] for key in set(l)}
for i in range(E):
    tree[l[2 * i]].append(l[2 * i + 1])
root_set = set(tree.keys()) - set(sum(tree.values(), []))
root = root_set.pop()

dfs(root, '+', 0, 0, [''])
