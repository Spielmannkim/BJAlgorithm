A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C)) # result라는 변수에 A,B,C의 곱을 문자열형태로 list에 차례차례 담는다.
for i in range(10): # 1부터 9까지의 수를 차례로 변수i에 담는다.
    print(result.count(str(i))) # i를 문자열화 시켜서 해당 result 배열에 i와 같은 값의 개수를 구해서 출력 후 for문을 반복한다.
