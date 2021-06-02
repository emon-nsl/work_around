import numpy as np

N, M, _ = [int(x) for x in input().strip().split()]
a, b = map(lambda x: np.array([input().strip().split() for i in range(int(x))], int), [N, M])
print(np.concatenate((a, b), axis = 0))
