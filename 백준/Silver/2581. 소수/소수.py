m = int(input())
n = int(input())
# m 이상 n 이하 자연수 중 소수를 모두 찾아 합을 변수 s에 저장 후 출력
# 소수 중 최솟값을 변수 mini에 저장 후 출력
sosu_list = [] # 소수 리스트
for num in range(m,n+1): # 최소값 부터 최대값까지 하나씩 num에 입력
    error = 0 # 변수 error는 0
    if num > 1: # 만약 변수 num이 1보다 크다면?
        for i in range(2, num): # 2부터 num까지 i에 입력
            if num % i == 0: # 만약 num / i의 나머지가 0이라면?
                error += 1 # error에 1을 더한다.
                break # 브레이크
        if error == 0: # 만약 error가 0이라면?
            sosu_list.append(num) # 소수리스트에 num을 요소로 추가
if len(sosu_list) > 0: # 만약 소수리스트의 개수가 0보다 크다면?
    print(sum(sosu_list)) # 모든 소수리스트를 더하여 출력
    print(min(sosu_list)) # 소수리스트중 최솟값을 출력
else:
    print(-1) # 소수가 없다면 -1을 출력