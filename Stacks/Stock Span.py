
from sys import stdin

def stockSpan(price, n) :
    S = [None]*n
    S[0] = 1
	#Your code goes here
    for i in range(1, n, 1): 
        S[i] = 1    
        j = i - 1
        while (j>= 0) and (price[i] > price[j]) : 
                       S[i] = S[i] + 1
                       j = j - 1
    return S
            

'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
