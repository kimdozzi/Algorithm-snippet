# 제곱수인지 아닌지 판별하는 코드 (다시보기)
import math
if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    sum = 1
    # flag = True
    for number in numbers:
        sum *= number
        print(math.sqrt(sum), int(math.sqrt(sum)))
        if math.sqrt(sum) == int(math.sqrt(sum)):  # 자연수인지 아닌지를 판별
            # 즉, 현재 만들어진 수가 제곱수인지 아닌지!
            # flag = False
            print('found')
            break
    else:
        print('not found')

    # if flag :
        # print('not found')

# -------------------------------------------------------------------------
# 가장 큰수, inf
min_val = float('inf')
max_val = float('-inf')
# -------------------------------------------------------------------------
