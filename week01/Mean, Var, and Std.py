import numpy as np
# np.set_printoptions(legacy='1.13')
def s2l(st):
    l = []
    st = st.split()
    for i in st:
        l.append(int(i))
    return l

n, m = map(int, input().split())
npar = np.array([s2l(input()) for _ in range(m)])
# print(npar)
mn = np.mean(npar, axis=1)
v = np.var(npar, axis=0)
sd =  np.std(npar, axis=None)
asd = np.around(sd, 11)

print(mn)
print(v)
print(asd)
