number_list = []# [10, 50, 15, 12, 8]
que = []
def pop_bigger(val):
    while len(que) and que[0]>val:
        que.pop(0)
def s2l(st):
    l = []
    st = st.split()
    for i in st:
        l.append(int(i))
    return l

n = int(input()) #size of the sub-array 
number_list = s2l(input())
print(number_list)
# que.append(number_list[0])
for i in range(0, n):
    pop_bigger(number_list[i])
    que.insert(0, number_list[i])
print(que)
print(que[len(que)-1])
k = 0
for i in range(1, len(number_list)-n+1):
    #this portion is to delete out of boundery value from our list
    for j in range(len(que)):
        if que[j] ==number_list[k]:
            que.pop(j)
            break
    k +=1
    pop_bigger(number_list[i+n-1])
    que.insert(0, number_list[i+n-1])
    print('printing ',que[len(que) - 1])
    # print('list ', que)

