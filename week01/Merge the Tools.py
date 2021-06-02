def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        l = []
        for j in range(k):
            if string[i+j] not in l:
                l.append(string[i+j])
        for item in l:
            print(item, end="")
        print()
        # i = i + k
        # print(i)

