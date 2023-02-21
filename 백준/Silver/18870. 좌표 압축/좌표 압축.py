n = int(input())
x = list(map(int, input().split()))
xset = set(x)
listx = list(xset)
listx.sort()
# 0부터 listx의 개수에 해당하는 키값을 하나씩 부여 후 x와 listx의 값이 같을 경우 키값을 출력
key_value={}
for i, num in enumerate(listx): # enumerate라는 함수는 더 써봐야 익숙해 질 것 같다.
    key_value[num] = i

xx=[]
for num in x:
    if num in key_value:
        xx.append(key_value[num])
print(*xx)
