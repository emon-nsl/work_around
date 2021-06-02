import re
for _ in range(int(input())):
    ptrn = input()
    ans = re.match(r'^[-+]?[0-9]*\.[0-9]+$', ptrn)
    print(bool(ans))