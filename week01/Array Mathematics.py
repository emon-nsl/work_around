import numpy as np
def s2l(st):
    l = []
    st = st.split()
    for i in st:
        l.append(int(i))
    return l
n, m = map(int, input().split())
# l = []
# for _ in range(n):
#     l.append(s2l(input()))
# a = np.array(l)
# l= []
# for _ in range(n):
#     l.append(s2l(input()))
# b = np.array(l)
a, b = (np.array([s2l(input()) for _ in range(n)]) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
