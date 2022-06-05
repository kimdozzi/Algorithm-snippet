# 문자열 자주 나오는 문제
# 1. 회문(Palindrome) - isalnum()으로 문자 및 공백 제거 후 list 또는 deque를 사용하기

# 2. 문자열 뒤집기 - s.reverse() 또는 투 포인터를 이용한 스왑 활용

# 3. 조건에 맞게 재정렬 - 조건에 맞게 분리 또는 초기화 후 정렬

# 4. 특정 문자/ 단어 추출
# 5. Counter
# 6. 애너그램(문자열 재배열 후 다른 뜻을 가진 단어로 바꿈)
# 7. 가장 긴 팰린드롬 찾기

# 문자열 정렬하기 - ljust, center, rjust
from collections import defaultdict
import collections
import string
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

# 알파벳 출력하기 - string 모듈
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)

# 문자열 연결하기
my_list = ['1', '100', '33']
answer = ''.join(my_list)

# ----------------------------------------------------------------------------
# collections.counter 사용하기
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1,
           2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)
print(answer[1])  # = 4
print(answer[3])  # = 3


# 가장 많이 나오는 알파벳 수 추출
my_str = input().strip()
answer = collections.Counter(list(my_str))
maxnum = max(answer.values())
lst = []
result = ''
for k, v in answer.items():
    if maxnum == v:
        lst.append(k)
for i in sorted(lst):
    result += i
print(result)  # aabbc => ab

# most_common() 함수 사용하기
my_str = input().strip()
answer = collections.Counter(my_str)
MAX = 0
MAX_str = ''
for x, a in answer.most_common():
    if a >= MAX:
        MAX = a
        MAX_str += x
MAX_str = ''.join(sorted(MAX_str))
print(MAX_str)
# --------------------------------------------------------
# collections.defaultdict 사용하기 
def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter


# 사전 기본값으로 빈 리스트 세팅하기
def groupWords(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper


# defaultdict 클래스없이 구현한 경우
def groupWords(words):
    grouper = {}
    for word in words:
        length = len(word)
        if length not in grouper:
            grouper[length] = []
        grouper[length].append(word)
    return grouper
# -------------------------------------------------------------------
