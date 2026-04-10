import csv
import random
import sys

# push recursion limit up since python's default (1000) can cause issues for large inputs
sys.setrecursionlimit(200000)

class Homework4:

    # QUESTION 1
    # Implement randomized quicksort and heapsort in the below function
    # Input for the function - an array of floating point numbers ex: [3.0,9.0,1.0]
    # Output - sorted list of numbers ex: [1.0,3.0,9.0]
    # Numbers can be negative, repeated, and floating point numbers
    # DO NOT USE THE INBUILT HEAPQ MODULE TO SOLVE THE PROBLEMS

    def randomQuickSort(self, nums: list) -> list:
        arrCopy = nums.copy()
        self._quicksort(arrCopy, 0, len(arrCopy) - 1)
        return arrCopy

    def _randomizedPartition(self, arr, low, high):
        # swap a random element into the pivot position
        randIdx = random.randint(low, high)
        arr[randIdx], arr[high] = arr[high], arr[randIdx]
        return self._partition(arr, low, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(self, arr, low, high):
        if low < high:
            pivotIdx = self._randomizedPartition(arr, low, high)
            self._quicksort(arr, low, pivotIdx - 1)
            self._quicksort(arr, pivotIdx + 1, high)

    def heapSort(self, nums: list) -> list:
        arrCopy = nums.copy()
        self._buildMaxHeap(arrCopy)
        n = len(arrCopy)
        for i in range(n - 1, 0, -1):
            # move current max to end
            arrCopy[0], arrCopy[i] = arrCopy[i], arrCopy[0]
            self._heapify(arrCopy, i, 0)
        return arrCopy

    def _buildMaxHeap(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

    def _heapify(self, arr, heapSize, rootIdx):
        largest = rootIdx
        leftChild = 2 * rootIdx + 1
        rightChild = 2 * rootIdx + 2

        if leftChild < heapSize and arr[leftChild] > arr[largest]:
            largest = leftChild
        if rightChild < heapSize and arr[rightChild] > arr[largest]:
            largest = rightChild

        if largest != rootIdx:
            arr[rootIdx], arr[largest] = arr[largest], arr[rootIdx]
            self._heapify(arr, heapSize, largest)


# Main Function
# Do not edit the code below
if __name__ == "__main__":
    homework4  = Homework4()
    testCasesforSorting = []
    try:
        with open('testcases.csv','r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testCasesforSorting.append(row)
    except FileNotFoundError:
        print("File Not Found") 
    
    # Running Test Cases for Question 1
    print("RUNNING TEST CASES FOR QUICKSORT: ")
    
    for row , (inputValue,expectedOutput) in enumerate(testCasesforSorting,start=1):
        if(inputValue=="" and expectedOutput==""):
            inputValue=[]
            expectedOutput=[]
        else:
            inputValue=inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput=expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.randomQuickSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if(are_equal):
            print(f"Test Case {row} : PASSED")
        else:
             print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")
    
    print("\nRUNNING TEST CASES FOR HEAPSORT: ")         
    for row , (inputValue,expectedOutput) in enumerate(testCasesforSorting,start=1):
        if(inputValue=="" and expectedOutput==""):
            inputValue=[]
            expectedOutput=[]
        else:
            inputValue=inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput=expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.heapSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if(are_equal):
            print(f"Test Case {row} : PASSED")
        else:
             print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")