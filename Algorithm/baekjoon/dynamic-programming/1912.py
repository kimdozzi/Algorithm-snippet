import sys
N = int(input())
dp = list(map(int,sys.stdin.readline().split()))
for i in range(1, len(dp)) :
    dp[i] = max(dp[i], dp[i]+dp[i-1])
print(max(dp))