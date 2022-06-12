# list comprehension의 기본 문법
# '''[(변수를 활용한 값) for (사용할 변수 이름) in (순회할 수 있는 값)]
# 기존 방법 '''
size = 10
arr = [0] * size
for i in range(size):
    arr[i] = i * 2
print(arr)
# '''리스트 컴프리핸션을 사용한 기본 문법'''
arr2 = [i * 2 for i in range(size)]
print(arr2)


# 조건문으로 필터링하기
arr3 = [n for n in range(1, 11) if n % 2 == 0]
print(arr3)
# '''조건문 여러개 사용하기
# # and statement를 사용하면 `syntax error` 발생
# # 만약 and 또는 or을 사용하고 싶은 경우 하나의 if문에서 연산자 사용하기'''
arr4 = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
print(arr4)
arr5 = [n for n in range(1, 31) if n % 2 == 0 and n % 3 == 0]
print(arr5)


# 2차원 배열에서의 활용(차원의 축소)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          ]
# '''1차원으로 축소'''
flat_one = [n for row in matrix for n in row]
# '''리스트 컴프리핸션을 사용하지 않은 방법'''
flat_one2 = []
for row in matrix:
    for n in row:
        flat_one2.append(n)
print(matrix)
print(flat_one)
print(flat_one2)


# 4x3 행렬 구조를 유지하면서 각 셀의 값을 제곱하기
# '''[n**2 for n in row]를 A로 치환하면 쉽게 생각할 수 있다.
# 즉, squared_list = [ A for row in matrix ]
# 위의 두 예제가 헷갈린다.
# 하지만, 자주 사용하는 방법은 아니므로 알고만 있자.'''
squared_list = [[n**2 for n in row] for row in matrix]
print(squared_list)


# 다른 자료구조로의 확장
# from string import ascii_lowercase as LOWERS
dict_boy = {c: n for c, n in zip(LOWERS, range(1, 27))}
print(dict_boy)
print(dict(zip(LOWERS, range(1, len(LOWERS)+1))))
