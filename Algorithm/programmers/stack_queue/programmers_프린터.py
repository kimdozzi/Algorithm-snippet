def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])


    while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
          print(d)

      else:
          answer += 1
          if item[1] == location:
              break
    return answer

priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities,location))





# 다른 사람 코드
from collections import deque


def solution(priorities, location):
    cnt = 0
    queue = deque()
    for i, v in enumerate(priorities):
        queue.append((i, v))

    while queue:
        max_value = max(queue, key=lambda x: x[1])[1]
        idx, value = queue.popleft()

        if value == max_value:
            cnt += 1
            if idx == location:
                break
        else:
            queue.append((idx, value))

    return cnt


