def is_prime(n): # 소수인지 확인하는 함수 is_prime()
    if n == 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

# n을 반으로 쪼개서 하나는 +1씩 해주고 하나는 -1씩해서 동시에 소수가 되는 지점 찾기

t = int(input())
for _ in range(t):
    n = int(input())
    
    a = n//2
    b = n//2
    while a > 0: # a는 0보다 커야함
        if is_prime(a) and is_prime(b): # 만약 a,b둘다 소수 일 경우 프린트하고 브레이크
            print(a,b)
            break
        else: # 아닐경우 a는 하나빼고 b는 하나빼서 다시 둘다 소수인지 판별
            a -= 1
            b += 1