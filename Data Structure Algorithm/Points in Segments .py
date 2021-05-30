def searchLowerBound(array, key):
	begin=0
	end=len(array)-1
	index=-1
	while begin<=end:
		mid=(begin+end)//2
		if key == array[mid]: 
			index=mid
			end=mid-1
		elif key > array[mid]: begin=mid+1
		elif key < array[mid]: end=mid-1
	return begin
	
def searchUperBound(array, key):
	begin=0
	end=len(array)-1
	index=-1
	while begin<=end:
		mid=(begin+end)//2
		if key == array[mid]: 
			index=mid
			begin=mid+1
		elif key > array[mid]: begin=mid+1
		elif key < array[mid]: end=mid-1
	return begin


test_case = int(input())
for t in range(test_case):
    print('Case {}:'.format(t+1))
    _ = list(map(int,input().strip().split()))[:2]
    n, q = _[0], _[1]
    # print(n, q)
    l = input()
    given_li = [int(i) for i in l.split(' ')]
    info=sorted(given_li)
    # print (info)
    for i in range(q):
        _ = list(map(int,input().strip().split()))[:2]
        x, y = _[0], _[1]
        lower= searchLowerBound(info,x)
        uper = searchUperBound(info, y)
        # print('lowerbound is ', lower, ' upper ', uper)
        print(uper - lower)