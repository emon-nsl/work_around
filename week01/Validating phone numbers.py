import re
for i in range(int(input())):
    ans = re.match(r'[789]\d{9}$', input())
    if ans:
        print('YES')
    else:
        print('NO')
