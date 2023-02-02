A, B = [], [] # a,b 두 행렬 선언

N, M = map(int, input().split()) # 행렬의 크기 n가로 m세로

for _ in range(N): # N번 반복
    row = list(map(int, input().split())) # row에 리스트 입력 요소는 n개
    A.append(row) # 받은 리스트row를 A행렬에 추가

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row) # 받은 리스트row를 B행렬에 추가

#16줄을 지금은 이해하기 어렵다.
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()