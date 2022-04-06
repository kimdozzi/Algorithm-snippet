# 이분 탐색 문제 => dp로 풀면 시간초과 
# 그 이유는 모든 경우의 수를 모두 탐색하므로 
import bisect
x = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))