def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        lst = sorted(array[i - 1:j])
        answer.append(lst[k - 1])
        
    return answer