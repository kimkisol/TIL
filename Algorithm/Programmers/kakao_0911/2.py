def solution(n, k):
    nk = []
    while n > 0:
        nk.append(n % k)
        n //= k
    if len(nk) == 1 and nk[0] == 1:
        return 0
    nk.reverse()
    str_n = ''
    int_n = []
    for i in range(len(nk)):
        if nk[i] != 0:
            str_n += str(nk[i])
            if i == len(nk) - 1 and str_n != '1' and str_n:
                int_n.append(int(str_n))
                str_n = ''
            continue
        elif str_n != '1' and str_n:
            int_n.append(int(str_n))
        str_n = ''

    for i in range(len(int_n)):
        if int_n[i] == 2:
            int_n[i] = 1
            continue
        for div_n in range(2, int(int_n[i] ** 0.5) + 1):
            if int_n[i] % div_n == 0:
                int_n[i] = 0
                break
        else:
            int_n[i] = 1

    return sum(int_n)


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(1000000, 3))
