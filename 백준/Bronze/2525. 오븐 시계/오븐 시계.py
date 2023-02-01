a,b=map(int, input().split())
c = int(input())

hour = (b+c)//60 # 몫 이 곧 더해지는 시간
min = (b+c)%60 # 나머지가 곧 분

if(b+c >= 60):
    if(a+hour >= 24):
        a = a-24
    a = a+hour
    print(a, min)

else:
    if(a >= 24):
        a = a-24
    print(a, b+c)