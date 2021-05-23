# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    l = len(string)
    if l == 0 or l == 1:
        return string
    
    smallOutput = removeConsecutiveDuplicates(string[1:])
    if string[0] == smallOutput[0]:
        return smallOutput
    else:
        return string[0] + smallOutput
       

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
