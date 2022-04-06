import sys
S = sys.stdin.readline().rstrip()
Prec = {'*':3, '/':3, '+':2, '-':2, '(':1}
stack = []
for i in S :
    if i.isalpha():
        print(i,end='')
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            print(temp,end='')
    elif i in '*/+-':
        while stack and Prec[stack[-1]] >= Prec[i]:
            print(stack.pop(),end='')
        stack.append(i)

while stack:
    print(stack.pop(),end='')