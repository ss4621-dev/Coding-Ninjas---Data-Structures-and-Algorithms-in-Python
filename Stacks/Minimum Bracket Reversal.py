
from sys import stdin

def countBracketReversals(inputString) :
    # Your code goes here
    if(len(inputString) == 0):
        return 0
    if(len(inputString) % 2 != 0):
        return -1
    
    s = []
    for ele in inputString:
        if ele == '{':
            s.append(ele)
        else:
            if(len(s) > 0 and s[-1] == '{'):
                s.pop()
            else:
                s.append(ele)
    count = 0
    while(len(s) != 0):
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count += 2
        else:
            count += 1
    return count
    


#main
print(countBracketReversals(stdin.readline().strip()))
