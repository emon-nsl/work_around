import numpy

n, m = map(int, input().split())
ar = numpy.array([input().strip().split() for _ in range(n)], int)
print (ar.transpose())
print (ar.flatten())
