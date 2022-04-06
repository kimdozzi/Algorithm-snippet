import sys
s = sys.stdin.readline().rstrip()
Max = Min = ''
num = 0
for i in range(len(s)) :
    if s[i] == 'M':
        num += 1
    elif s[i] == 'K':
        if num :
            Min += str(10 ** num + 5)
            Max += str(5 * (10 ** num))
        else:
            Min += '5'
            Max += '5'
        num = 0

if num :
    Min += str(10 ** (num - 1))
    Max += '1' * num

print(Max)
print(Min)
