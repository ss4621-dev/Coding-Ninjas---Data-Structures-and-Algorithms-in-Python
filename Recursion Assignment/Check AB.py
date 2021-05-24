## Read input as specified in the question.
## Print output as specified in the question.
def checkAb(s):
    if len(s) == 0:
        return True
    if s[0] == 'a':	
        if len(s[1:]) == 0:
            return True
        else:
            if s[1] == 'a':
                return checkAb(s[1:])
            else:
                if s[2] == 'b':
                    return checkAb(s[3:])
                else:
                    return False
        
    else:
        return False


#main
s = input()
if checkAb(s):
    print('true')
else:
    print('false')
