T = int(input())
for i in range(T):
    re, S = input().split()
    text = ''
    for i in S:
        text += int(re) * i
    print(text)