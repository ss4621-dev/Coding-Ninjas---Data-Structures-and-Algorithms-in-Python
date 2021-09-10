
import sys
from sys import setrecursionlimit
setrecursionlimit(10**6)

        
def printPermutations(string,op):
    #base case
    if len(string)==0:
        print(op)
        return
    
    for i in range(0,len(string)):
        printPermutations(string[:i] + string[i+1:], op + string[i])
        
#main
string = input()
printPermutations(string, '')
