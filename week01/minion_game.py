def minion_game(string):
    vowel = ('A', 'E', 'I', 'O', 'U')
    # print(string)
    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in vowel:
            k += len(string) - i
        else:
            s += len(string) - i
    
    if k > s:
        print('Kevin ' + str(k))
        # print(s)
    elif k ==s:
        print('Draw')
    else:
        # print(k)
        print('Stuart ' + str(s)) 
if __name__ == '__main__':
    s = input()
    minion_game(s)