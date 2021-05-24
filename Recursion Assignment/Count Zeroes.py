## Read input as specified in the question.
## Print output as specified in the question.
def zeroes(n, cnt):
    if n == 0:
        return cnt

    elif n % 10 == 0:
        return zeroes(n//10, cnt+1)

    else:
        return zeroes(n//10, cnt)


n = int(input())
if n == 0:
    print(1)
else:
	print(zeroes(n, 0))
