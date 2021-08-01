tries = int(input())
thirty = [4, 6, 9, 11]

for i in range(tries):
    date = input()
    month = int(date[4 : 6])
    day = int(date[6 : 8])
    print(f'#{i + 1}', end=' ')
    if month < 1 or month > 12 or day < 1 or day > 31:
        print(-1)
        continue
    elif month == 2:
        if day > 28:
            print(-1)
            continue
    elif month in thirty:
        if day > 30:
            print(-1)
            continue
    print(date[0 : 4] + '/' + date[4 : 6] + '/' + date[6 : 8])
        
            