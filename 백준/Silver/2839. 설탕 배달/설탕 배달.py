sugar = int(input()) # 설탕 N키로그램을 배달해야한다.

bag = 0 # 가방의 개수

while sugar >= 0: # 설탕이 0이상일 때
    if sugar % 5 == 0: # 5의 배수이면
        bag += (sugar // 5) # 5로 나눈 몫을 가방의 개수에 더한다.
        print(bag) # 가방의 개수 출력
        break # 6줄의 if조건이 성립할 때 5줄부터 시작된 while문 탈출
    
    # break탈출 했다는건 5의 배수가 아니라는뜻, 5의 배수가 될 때까지 설탕-3, 가방+1
    sugar -= 3
    bag += 1 
else:
    print(-1) # 가방에 넣을 수 없을 경우 -1 출력
