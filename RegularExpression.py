def isMatch(text, pattern):
    T = [[]]
    T[0] = [True]
    for i in range(1,len(pattern)+1):
        if(pattern[i-1]=="*"):
            T[0].append(T[0][i-2])
        else:
            T[0].append(False)
    for i in range(len(text)):
        T.append([False])
    for i in range(1, len(text)+1):
        for j in range(1, len(pattern)+1):
            if(text[i-1]==pattern[j-1] or pattern[j-1]=='.'):
                T[i].append(T[i-1][j-1])
            elif (pattern[j-1]=='*'):
                T[i].append(T[i][j-2])
                if (text[i-1]==pattern[j-2] or pattern[j-2]=="."):
                    T[i][j] = T[i][j] or T[i-1][j]
            else:
                T[i].append(False)
    print(T)
    return T[len(text)][len(pattern)]

print(isMatch("a","a."))