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

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

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

w = open('algtest.txt', 'w')

sorted_list = list(range(1, 10000))
sorted_listcopy = sorted_list.copy()

reverse_list = sorted_list.copy()
reverse_list.reverse()
reverse_listcopy = reverse_list.copy()

ave_list = []
for i in range(100):
    ave_list.append([])
for i in range(100):
    for j in range(10000):
        ave_list[i].append(j)
for i in range(100):
    random.shuffle(ave_list[i])


totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0

for x in range(1):
    #B best case is sorted
    
    sorted_list = sorted_listcopy.copy()
    
    ave_listb = ave_list[x].copy()
    
    #B worst case is reverse sorted
    reverse_list = reverse_listcopy.copy()
    
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
    
    start = time.perf_counter_ns()
    bubbleSort(reverse_list)
    stop = time.perf_counter_ns()
    #print(worst_list)
    duration = (stop - start)
    #print("Bubble sort completed " + str(duration) + " seconds")
    totalw = totalw + duration
   
averageb = truncate(((totalb/100)* 10**-9), 7)
w.write("Bubble sort best time complexity average is: " + str(averageb) + " seconds")
averagea = truncate(((totala/100)* 10**-9), 7)
w.write("Bubble sort average time complexity is: " + str(averagea) + " seconds")
averagew = truncate(((totalw/100)* 10**-9), 7)
w.write("Bubble sort worst time complexity average is: " + str(averagew) + " seconds") 
   
totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0

for x in range(100):
    
    ave_listm = ave_list[x].copy()
    
    start = time.perf_counter_ns()
    mergeSort(ave_listm)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Merge sort completed " + str(duration) + " seconds")
    totala = totala + duration

averagea = truncate(((totala/100)* 10**-9), 7)
w.write("Merge sort average time complexity is: " + str(averagea) + " seconds")

totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0
    
for x in range(100):
    low = 0
    high = 9998
    
    #Q average case is random array
    ave_listq = ave_list[x].copy()
    
    #Q worst case is sorted
    worst_list = sorted_listcopy.copy()
    
    start = time.perf_counter_ns()
    quickSort(ave_listq, low, high)
    stop = time.perf_counter_ns()
    #print(ave_list)
    duration = (stop - start)
    #print("Quick sort completed " + str(duration) + " seconds")
    totala = totala + duration
    
    start = time.perf_counter_ns()
    quickSort(worst_list, low, high)
    stop = time.perf_counter_ns()
    #print(worst_list)
    duration = (stop - start)
    #print("Quick sort completed " + str(duration) + " seconds")
    totalw = totalw + duration

averagea = truncate(((totala/100)* 10**-9), 7)
w.write("Quick sort average time complexity is: " + str(averagea) + " seconds")
averagew = truncate(((totalw/100)* 10**-9), 7)
w.write("Quick sort worst time complexity average is: " + str(averagew) + " seconds")

totalb = 0
averageb = 0
totala = 0
averagea = 0
totalw = 0
averagew = 0    

for x in range(1):
      
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
    
averageb = truncate(((totalb/100)* 10**-9), 7)
w.write("Insertion sort best time complexity average is: " + str(averageb) + " seconds")
averagea = truncate(((totala/100)* 10**-9), 7)
w.write("Insertion sort average time complexity is: " + str(averagea) + " seconds")

# duration = truncate(((stop - start)* 10**-9), 7)