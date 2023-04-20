T = int(input())
for _ in range(T):
    arr = list(input())
    sum = 0
    for i in arr:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: # sum이 음의정수가 되면 NO하고 for문 탈출
            print('NO')
            break
    if sum > 0: # sum이 양의정수면 NO
        print('NO')
    elif sum == 0: # sum이 0이면 YES
        print('YES')
