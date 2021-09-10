def subsequences(string):
    if string == '':
        return ['']
    
    ans = subsequences(string[1:])
    curr = string[0]
    n = len(ans)
    for i in range(0,n):
        ans.append(curr+ans[i])
    return ans


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
