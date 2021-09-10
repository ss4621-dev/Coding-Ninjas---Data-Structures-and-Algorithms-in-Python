## Read input as specified in the question.
## Print output as specified in the question.
def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "

def printKeypad(n, output):
    if n == 0:
        print(output)
        return
    
    smallerNumber = n // 10
    lastDigit = n % 10
    
    optionsForLastDigit = getString(lastDigit)
    for c in optionsForLastDigit:
        newOutput = c + output
        printKeypad(smallerNumber, newOutput)
        
n = int(input())
ans = printKeypad(n, '')

