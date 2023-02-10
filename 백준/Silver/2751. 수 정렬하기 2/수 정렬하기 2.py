# n = int(input())
# li=[]
# for _ in range(n):
#     a = int(input())
#     li.append(a)
# sort_li = sorted(li)
# for i in sort_li:
#     print(i)

# 이 문제 부턴 위처럼 input()으로 받으면 시간초과가 걸리기에 sys.stdin.readline()을 써야한다.

import sys

n = int(input())
li=[]
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)