# bottom - up 방식
import sys
n = int(sys.stdin.readline())
dp = [0] * 1000001
dp[0], dp[1] = 0, 0
for i in range(2,n+1) :
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])



# top - down 방식
def top_down(n):         # 1을 뺐을 경우, 2를 나눈 경우, 3을 나눈 경우 => 총 3번의 계산을 모두 수행하여 그 중 최소값을 저장하고 리턴
    if n == 1:
        return 0
    if d[n] > 0: # 메모, 즉 값이 저장된 적이 있다면 그 값을 반환한다.
        return d[n]

    d[n] = top_down(n-1) + 1 # 1을 뺀 값을 저장 
    if n % 2 == 0:
        temp = top_down(n//2) + 1 # 2를 나눈 값을 temp에 저장
        if d[n] > temp: # 두 값을 비교하여 d[n]이 크면, 즉 1을 뺀 횟수보다 나눈 횟수가 더 적으면  
            d[n] = temp # 나눈 횟수를 dp에 저장
            
    if n % 3 == 0: # 위와 동일
        temp = top_down(n//3) + 1 
        if d[n] > temp:
            d[n] = temp
    return d[n]

n = int(sys.stdin.readline())
d = [0]*(n+1)
print(top_down(n))

