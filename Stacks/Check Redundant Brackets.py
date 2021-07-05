
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
    s = []
    flag = False
    for i in expression:
        if i == ')':
            count = 0
            while s.pop() != '(':
                count += 1
                
            if (count <=1 and flag == False) or count == 0:
                return True
            else:
                flag = True
            
            
        else:
            s.append(i)
            
    return False

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
