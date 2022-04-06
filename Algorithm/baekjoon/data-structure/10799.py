S = input().rstrip()
stack = []
cnt = 0

for i in range(len(S)) :
    if S[i] == '(':
        stack.append('(')
    else:
        if S[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)