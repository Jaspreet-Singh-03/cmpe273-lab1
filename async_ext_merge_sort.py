import os.path
import heapq
import asyncio

async def mergeSort (usList , left , right):
    if left < right:
        mid = left + ((right - left)/2)
        mid = int(mid)
        await mergeSort(usList, left, mid)
        await mergeSort(usList, mid + 1, right)
        await merge(usList, left, mid, right)

async def merge(usList , left, mid, right):
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

async def sort(i):
    fileName = os.getcwd()+os.path.sep+"input/unsorted_%d.txt"%i
    with open(fileName,"r") as inputFile:
        usList = inputFile.readlines()
        usList= [int(x) for x in usList]
    inputFile.close()
    n=len(usList)
    await mergeSort(usList, 0, n-1)
    listofLists.append(usList)

async def main():
    
    sortedList = list(heapq.merge(*listofLists))  
    fileName2 = os.getcwd()+os.path.sep+"output/async_sorted.txt"  
    with open(fileName2, "w") as outputFile:
        for x in sortedList:
            outputFile.write(str(x) + '\n')
        outputFile.close()

loop = asyncio.get_event_loop()
task = [0]*10
for i in range(0,10):
    task[i] = loop.create_task(sort(i+1))    
loop.run_until_complete(asyncio.gather(*task))
asyncio.run(main())
