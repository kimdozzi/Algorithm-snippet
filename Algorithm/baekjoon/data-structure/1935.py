N = int(input())
string = input()
alpha = [0] * N

for i in range(N) :
    alpha[i] = int(input())

stack = []
for i in string:
    if i.isalpha():
        stack.append(alpha[ord(i) - ord('A')])

    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+' :
            stack.append(str1 + str2)
        elif i == '-' :
            stack.append(str1 - str2)
        elif i == '*' :
            stack.append(str1 * str2)
        elif i == '/' :
            stack.append(str1 / str2)

print('%.2f'%stack[0])