n = int(input()) # 테케
arr = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age,name)) # 리스트에 요소 두개씩 받을 때 이렇게 append하는거 제발 까먹지좀 말자..
arr.sort(key = lambda x: x[0]) # age 자리에 입력되는 요소를 기준으로 sort한 후
for i in arr:
    print(i[0],i[1]) # age, name을 하나씩 출력하면 된다.

# 처음에 순서대로 입력받았으니 입력순은 구지 입력해주지 않아도 된다.