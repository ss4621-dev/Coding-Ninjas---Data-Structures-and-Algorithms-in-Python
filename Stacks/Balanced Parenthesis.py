
from sys import stdin


def isBalanced(expression) :
	#Your code goes here
    l = []
    for i in expression:
        if i in '({[':
            l.append(i)
        
        elif i == ')':
            if(not l or l[-1]!='('):
                return False
            l.pop()
        
        elif i == '}':
            if (not l or l[-1]!= '{'):
                return False
            l.pop()
            
        elif i == ']':
            if(not l or l[-1]!= '['):
                return False
            l.pop()
    if not l:
        return True
    return False


#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
