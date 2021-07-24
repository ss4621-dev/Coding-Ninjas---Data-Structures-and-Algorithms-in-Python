def uniqueChar(s):
    l = {}
    for i in s:
        if i not in l:
            print(i, end='')
            l[i] = l.get(i, 0) + 1
# Main 
s=input() 
uniqueChar(s)
