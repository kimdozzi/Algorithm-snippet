# pythonic 한 코드 정리
# divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느리다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르다.
a, b = 7, 5
print(*divmod(a,b))

# 파이썬 제대로 활용 (int함수활용)
num = '3212'
base = 5
ans = int(num,base)


# 문자열 정렬하기 - ljust, center, rjust
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))


# 알파벳 출력하기 - string 모듈
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)


# 원본을 유지한 채, 정렬된 리스트 구하기 - sorted
list1 = [3,2,5,1]
list2 = sorted(list1)


