a, b = map(int, input().split()) # 전체a명중 b명이 상을 받는다.
score = list(map(int, input().split()))
score = sorted(score, reverse=True)
print(score[b-1])