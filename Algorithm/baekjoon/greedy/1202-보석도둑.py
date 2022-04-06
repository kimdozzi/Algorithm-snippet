# 내가 작성 및 참조해서 공부한 코드

import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewel.sort()
bags.sort()
temp = []
result = 0

for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -jewel[0][1])  # 최대힙
        heapq.heappop(jewel)
    if temp:
        result += heapq.heappop(temp)
    elif not jewel:
        break

print(-result)





# 다른사람이 작성한 코드 (원래 내가 짜고 싶었던 코드)
if __name__ == '__main__':
    N,M= map(int,(input().split()))
    jewel = []
    bag = []
    price = 0
    for _ in range(N):
        jewel.append(list(map(int,(input().split())))) #[무게, 가격]
    for _ in range(M):
        bag.append(int(input()))
    jewel.sort(key=lambda x:(x[1],x[0]), reverse=True)
    bag.sort()
    for i in jewel:
        for idx,j in enumerate(bag):
            print(idx, j)
            if i[0]<j:
                price += i[1]
                bag.pop(idx)
                break
            else: continue

    print(price)



