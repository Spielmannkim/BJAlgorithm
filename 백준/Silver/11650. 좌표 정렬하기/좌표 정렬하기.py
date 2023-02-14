# [(x0,y0),(x1,y1)---] 이런 2차원배열을 만든다.
# 배열의 x값중 제일 작은 수를 맨 앞으로 놓는다
# 만약 x값이 같은 경우라면 y값 중 제일 작은 값을 맨 앞으로 놓는다.
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
# 입력한 좌표를 리스트에 저장한 뒤, 좌표의 첫번째 요소(x좌표)를 우선순위로, 
# 같은 x좌표를 가진 좌표들은 두번째 요소(y좌표)로 정렬해줍니다.
arr.sort(key=lambda x: (x[0], x[1]))
# 정렬된 리스트를 하나씩 출력합니다.
for x, y in arr:
    print(x, y)

