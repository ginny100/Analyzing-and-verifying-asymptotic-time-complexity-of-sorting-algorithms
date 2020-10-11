import random
import time
import math

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

# This code is contributed by Mohit Kumra
# This function is same in both iterative and recursive 
def partition(arr, l, h): 
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l, h): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 
  
# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def quickSortIterative(arr, l, h): 
  
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

# This code is contributed by Mohit Kumra        
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

w = open('algtest8.txt', 'w')
w.truncate(0)

arraynum = 100000
testloopnum = 10

sorted_list = list(range(1, arraynum))
sorted_listcopy = sorted_list.copy()

# reverse_list = sorted_list.copy()
# reverse_list.reverse()
# reverse_listcopy = reverse_list.copy()

ave_list = []
for i in range(testloopnum):
    ave_list.append([])
for i in range(testloopnum):
    for j in range(1, arraynum):
        ave_list[i].append(j)
for i in range(testloopnum):
    random.shuffle(ave_list[i])

w.write("For " + str(testloopnum) + " loops and " + str(arraynum) + " array elements\n\n")

totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0

for x in range(testloopnum):
    #B best case is sorted
    
    sorted_list = sorted_listcopy.copy()
    
    ave_listb = ave_list[x].copy()
    
    #B worst case is reverse sorted
    # reverse_list = reverse_listcopy.copy()
    
    start = time.perf_counter_ns()
    bubbleSort(sorted_list)
    stop = time.perf_counter_ns()
    #print(best_list)
    duration = (stop - start)
    #print("Bubble sort completed " + str(duration) + " seconds")
    totalb = totalb + duration
    
    start = time.perf_counter_ns()
    bubbleSort(ave_listb)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Bubble sort completed " + str(duration) + " seconds")
    totala = totala + duration
    
    # start = time.perf_counter_ns()
    # bubbleSort(reverse_list)
    # stop = time.perf_counter_ns()
    # #print(worst_list)
    # duration = (stop - start)
    # #print("Bubble sort completed " + str(duration) + " seconds")
    # totalw = totalw + duration
   
averageb = truncate(((totalb/testloopnum)* 10**-9), 7)
w.write("Bubble sort best time complexity average is: " + str(averageb) + " seconds\n")
averagea = truncate(((totala/testloopnum)* 10**-9), 7)
w.write("Bubble sort average time complexity is: " + str(averagea) + " seconds\n\n")
# averagew = truncate(((totalw/testloopnum)* 10**-9), 7)
# w.write("Bubble sort worst time complexity average is: " + str(averagew) + " seconds\n\n") 
   
totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0

for x in range(testloopnum):
    
    ave_listm = ave_list[x].copy()
    
    start = time.perf_counter_ns()
    mergeSort(ave_listm)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Merge sort completed " + str(duration) + " seconds")
    totala = totala + duration

averagea = truncate(((totala/testloopnum)* 10**-9), 7)
w.write("Merge sort average time complexity is: " + str(averagea) + " seconds\n\n")

totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0
    
for x in range(testloopnum):
    low = 0
    high = arraynum - 2
    
    #Q average case is random array
    ave_listq = ave_list[x].copy()
    
    #Q worst case is sorted
    worst_list = sorted_listcopy.copy()
    
    start = time.perf_counter_ns()
    quickSortIterative(ave_listq, low, high)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Quick sort completed " + str(duration) + " seconds")
    totala = totala + duration
    
    start = time.perf_counter_ns()
    quickSortIterative(worst_list, low, high)
    stop = time.perf_counter_ns()
    #print(worst_list)
    duration = (stop - start)
    #print("Quick sort completed " + str(duration) + " seconds")
    totalw = totalw + duration

averagea = truncate(((totala/testloopnum)* 10**-9), 7)
w.write("Quick sort average time complexity is: " + str(averagea) + " seconds\n")
averagew = truncate(((totalw/testloopnum)* 10**-9), 7)
w.write("Quick sort worst time complexity average is: " + str(averagew) + " seconds\n\n")

totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0    

for x in range(testloopnum):
      
    #I best case is sorted
    best_list = sorted_listcopy.copy()
    
    ave_listi = ave_list[x].copy()
    
    start = time.perf_counter_ns()
    insertionSort(best_list)
    stop = time.perf_counter_ns()
    #print(best_list)
    duration = (stop - start)
    #print("Insertion sort completed " + str(duration) + " seconds")
    totalb = totalb + duration
    
    start = time.perf_counter_ns()
    insertionSort(ave_listi)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Insertion sort completed " + str(duration) + " seconds")
    totala = totala + duration
    
averageb = truncate(((totalb/testloopnum)* 10**-9), 7)
w.write("Insertion sort best time complexity average is: " + str(averageb) + " seconds\n")
averagea = truncate(((totala/testloopnum)* 10**-9), 7)
w.write("Insertion sort average time complexity is: " + str(averagea) + " seconds\n\n")

w.close()

# duration = truncate(((stop - start)* 10**-9), 7)