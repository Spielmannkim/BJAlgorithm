a,b,c=map(int,input().split())
if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))
# 1000+70x < 170x
# 1070 < 170 = False (1)
# 1700 < 1700 = False (10)
# 1770 < 1870 = True (11)
# x = 0
# while True:
#     x = x+1
#     if a+b*x < c*x:
#         break
# print(x)
# 손익분기점이 안나올 경우 -1 찍는법을 모르겠다..
# 애초에 while 문제가 아니었다..