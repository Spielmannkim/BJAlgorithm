h, m=map(int, input().split()) # 기존 알람시간 00시 00분
# 45분 이른 알람시간을 출력해야함
if m >= 45:
    m = m-45
    print(h,m)
elif m < 45 and h != 0:
    h = h-1
    m = m+15
    print(h,m)
elif h == 0 and m < 45:
    h = 23
    m = m+15
    print(h,m)
