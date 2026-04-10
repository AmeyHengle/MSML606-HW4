import csv
class Homework4:

# QUESTION 1
# Implement randomized quicksort and heapsort in the below function
# Input for the function - an array of floating point numbers ex: [3.0,9.0,1.0]
# Output - sorted list of numbers ex: [1.0,3.0,9.0]
# Numbers can be negative, repeated, and floating point numbers
# DO NOT USE THE INBUILT HEAPQ MODULE TO SOLVE THE PROBLEMS

def randomQuickSort(self,nums:list) -> list:
    # Todo: Implement randomized quicksort
    pass

def heapSort(self,nums:list) -> list:
    # Todo: Implement heapsort
        pass

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
 
