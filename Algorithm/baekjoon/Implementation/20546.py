import sys
cash = int(sys.stdin.readline())
stock = list(map(int,sys.stdin.readline().split()))
jh_cash, sm_cash = 0, 0
jh_stk, sm_stk = 0, 0
jh_cash += cash
sm_cash += cash
compare = stock[0]
high, low = 0, 3
for i in stock : # 준현
    if jh_cash == 0:
        break
    jh_stk += jh_cash // i
    jh_cash = jh_cash % i

for i in range(1,len(stock)) : # 성민
    if compare < stock[i] : # 전날 대비 가격이 오를 때
        low = 3
        high += 1
    elif compare > stock[i]: # 전날 대비 가격이 내려갈 때
        high = 0
        low -= 1
    else: # 가격이 같을 때
        continue
    compare = stock[i]

    if high >= 3: # 3일째 상승했을 경우
        if sm_stk == 0 :
            high = 0
            continue
        sm_cash = sm_stk * stock[i]
        sm_stk = 0
        high = 0

    if low <= 0: # 3일째 내려갔을 경우
        sm_stk += sm_cash // stock[i]
        sm_cash = sm_cash % stock[i]

result_jh = jh_cash + (stock[-1] * jh_stk)
result_sm = sm_cash + (stock[-1] * sm_stk)

if result_jh > result_sm :
    print('BNP')
elif result_jh < result_sm:
    print('TIMING')
else:
    print('SAMESAME')
