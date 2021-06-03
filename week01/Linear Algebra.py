# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
def s2l(st):
    l = []
    st = st.split()
    for i in st:
        l.append(float(i))
    return l

m = int(input())

ans = np.linalg.det(np.array([s2l(input()) for _ in range(m)]))
print(round(ans, 2))
