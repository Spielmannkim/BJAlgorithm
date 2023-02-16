# 11650문제와 다른점은 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순으로 출력하기다.

n = int(input()) # 점의 개수

arr = [] # 빈 배열 생성
for i in range(n): # n번 반복
    x, y = map(int, input().split()) # 좌표 평면 위 x와 y입력받기
    arr.append((x, y)) # [(x0,y0),(x1,x2),(x3,y3)...] arr 배열에 입력받은 x와y들을 2차원 배열로 입력
arr.sort(key=lambda x: (x[1], x[0])) # 람다 함수에서 x[0]는 x를 의미하고 x[1]은 y를 의미한다. 여기서 y를 우선으로 정렬하고 싶으니 x[1],x[0]순으로 배치하면 된다.
for x, y in arr:
    print(x, y)