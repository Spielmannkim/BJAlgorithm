m, n = map(int, input().split()) # 10~20으로 가정
sosu_list = [] # 소수 리스트

for num in range(m, n + 1):
    if num == 1: # 1은 소수가 아니므로 제외
        continue
    for i in range(2,int(num**0.5)+1): # 2부터 num의 제곱근+1을 i에 지정
        if num % i == 0: # 약수가 존재하므로 소수가 아님
            break
    else:
        print(num)