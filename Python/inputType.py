# 숫자의 각 자리수를 리스트로 변환
n = int(input())
lst = list(map(int, str(n)))

lst = [int(i) for i in str(int(input()))]


# 각 문자 사이에 공백이 없는 문자들을 입력받아 2차원 배열로 만들기
matrix = []
for i in range(n):
    matrix.append([s for s in (input().rstrip())])
