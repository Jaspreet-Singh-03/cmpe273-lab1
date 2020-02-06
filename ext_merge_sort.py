import os.path
import heapq

def mergeSort (usList , left , right):
    if left < right:
        mid = left + ((right - left)/2)
        mid = int(mid)
        mergeSort(usList, left, mid)
        mergeSort(usList, mid + 1, right)
        merge(usList, left, mid, right)

def merge(usList , left, mid, right):
    if left == right:
        return
    n1 = mid - left + 1
    n2 = right - mid
    leftarray = [0] * (n1)
    rightarray = [0] * (n2)

    for i in range(0, n1):
        leftarray[i] = usList[left + i]

    for j in range(0, n2):
        rightarray[j] = usList[mid + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if leftarray[i] >= rightarray[j]:
            usList[k] = rightarray[j]
            j = j + 1
            k = k + 1
        else:
            usList[k] = leftarray[i]
            i = i + 1
            k = k + 1

    while i < n1:
        usList[k] = leftarray[i]
        i = i + 1
        k = k + 1

    while j < n2:
        usList[k] = rightarray[j]
        j = j + 1
        k = k + 1

listofLists = []

def sort(i):
    fileName = os.getcwd()+os.path.sep+"input/unsorted_%d.txt"%i
    with open(fileName,"r") as inputFile:
        usList = inputFile.readlines()
        usList= [int(x) for x in usList]
    inputFile.close()
    n=len(usList)
    mergeSort(usList, 0, n-1)
    listofLists.append(usList)

def main():
    for i in range(0,10):
        sort(i+1)
    sortedList = list(heapq.merge(*listofLists)) 
    fileName2 = os.getcwd()+os.path.sep+"output/sorted.txt"  
    with open(fileName2, "w") as outputFile:
        for x in sortedList:
            outputFile.write(str(x) + '\n')
        outputFile.close()

if __name__== "__main__":
    main()
