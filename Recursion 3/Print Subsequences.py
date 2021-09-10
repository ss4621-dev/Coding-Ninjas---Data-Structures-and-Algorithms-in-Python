## Read input as specified in the question.
## Print output as specified in the question.

def printSubSequences(s,o):
    if len(s) == 0:
        print(o)
        return
    
    printSubSequences(s[1:], o)
    printSubSequences(s[1:], o+s[0])
    
    
#main
s = input()
ans = printSubSequences(s,'')

    
