# 전치행렬 만들기
'''보통의 방법'''
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[i][j])

# '''zip과 unpacking 활용'''
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(new_list)


# zip 활용하기
# '''다양한 사용 방법
# # This is similar to transposing a matrix. '''
for item in zip([1, 2, 3], ['sugar', 'spice', 'everthing']):
    print(item)
print(list(zip(range(3), ['fee', 'fi', 'fo', 'fum'])))


# 여러 개의 iterable 동시 순회할 때
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
    print(number1 + number2 + number3)


# key 리스트와 value 리스트로 딕셔너리 생성
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)
