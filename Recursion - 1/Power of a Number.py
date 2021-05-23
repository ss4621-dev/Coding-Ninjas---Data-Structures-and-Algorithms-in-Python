def power(x,n):
    if n == 0:
        return 1
    else:
        return (x * power(x, n-1))
    
    


ip = [int(i) for i in input().split()]
x = ip[0]
n = ip[1]
print(power(x, n))
