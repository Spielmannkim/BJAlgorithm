n = int(input()) # 단어의 개수
arr = []
for _ in range(n):
    word = input()
    arr.append(word)
arr_set = set(arr)
arr_list = list(arr_set)
arr_list.sort() # sort()를 하면 알파벳 순으로 정렬을 해준다...
arr_list.sort(key=len) # 알파벳 개수순으로 arr배열을 정렬
for i in arr_list:
    print(i)
