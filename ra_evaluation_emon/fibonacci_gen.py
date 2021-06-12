n = input("Please enter numbers of fibonacci number that you want:")
n = n.split(', ')
# print(n)
nl = [int(i) for i in n]
# print(nl)
for i in nl:
    a, b = 0, 1
    for _ in range(i):
        print(a, end = " ")
        a, b = b, a+b
    print()