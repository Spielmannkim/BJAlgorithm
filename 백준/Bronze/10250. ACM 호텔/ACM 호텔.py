# 호텔의 floor X rooms 층,방 개수가 주어지고 몇 번째 손님인지 주어졌을 때 손님의 방번호를 출력하라.

test = int(input()) # 테스트 개수

for _ in range(test):
    floor, rooms, customer = map(int, input().split()) # 테스트 개수만큼 층, 방, 손님 수를 입력받는다.
    oyy = customer // floor + 1 # 손님의 호실 첫째자리
    xoo = customer % floor # 손님의 객실 층 수
    if customer % floor == 0: # floor의 배수이면
        oyy = customer // floor # 배수인 경우 손님의 객실 호실번호
        xoo = floor # 배수인 경우 손님의 객실 층 번호
    print(f'{xoo*100+oyy}') # x에는 손님 객실의 층수에 해당하는 수, yy에는 손님의 호실넘버
    