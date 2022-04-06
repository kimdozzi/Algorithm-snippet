import sys
start_time = dict()
end_time = dict()
S, E, Q = map(str,input().split())
start = '0' + str(int(S[:2] + S[3:]))
end = E[:2] + E[3:]
end_st = Q[:2] + Q[3:]
cnt = 0
while True:
    try:
        chat_time, username = map(str, input().split())
        if len(chat_time) <= 1:
            break
        chat_time = chat_time.replace(':', '')

        if 0 <= int(chat_time) <= int(start) :
            start_time.setdefault(username, chat_time)
        elif int(end) <= int(chat_time) <= int(end_st) :
            end_time.setdefault(username, chat_time)

    except Exception as e:
        for i in start_time:
            if i in end_time:
                cnt += 1

        print(cnt)
        sys.exit(0)
