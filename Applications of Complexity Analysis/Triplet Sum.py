

from sys import stdin

def tripletSum(arr, n, num) :
    arr.sort()

    numTriplets = 0;

    for i in range(n) :
        pairSumFor = num - arr[i]
        numPairs = pairSum(arr, (i + 1), (n - 1), pairSumFor)

        numTriplets += numPairs

    return numTriplets


def pairSum(arr, startIndex, endIndex, num) :

    numPair = 0

    while startIndex < endIndex :

        if arr[startIndex] + arr[endIndex] < num :
            startIndex += 1

        elif arr[startIndex] + arr[endIndex] > num :
            endIndex -= 1

        else :

            elementAtStart = arr[startIndex]
            elementAtEnd = arr[endIndex]

            if elementAtStart == elementAtEnd :
                totalElementsFromStartToEnd = (endIndex - startIndex) + 1
                numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)

                return numPair

            tempStartIndex = startIndex + 1
            tempEndIndex = endIndex - 1

            while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart) :
                tempStartIndex += 1

            while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd) :
                tempEndIndex -= 1

            totalElementsFromStart = (tempStartIndex - startIndex)
            totalElementsFromEnd = (endIndex - tempEndIndex)

            numPair += (totalElementsFromStart * totalElementsFromEnd)

            startIndex = tempStartIndex
            endIndex = tempEndIndex


    return numPair




def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1
